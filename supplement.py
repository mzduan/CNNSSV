
#除了image的特征外，额外融入序列特征(hash sequence)，坐标信息，比对质量信息
import pysam
import numpy as np

def get_reverse_comp(s):
    ret=""
    for i in range(len(s)-1,-1,-1):
        if s[i]=='A':
            ret=ret+'T'
        elif s[i]=='T':
            ret=ret+'A'
        elif s[i]=='C':
            ret=ret+'G'
        elif s[i]=='G':
            ret=ret+'C'
    return ret
def get_somatic_kmer(sv_type,somatic_support_reads,normal_bam_file,ref_dict,chro,bk):


    ref_bk1=bk[0]
    ref_bk2=bk[0]+bk[1]
    if sv_type=="INS":
        ref_bk2=ref_bk1+1

    k=31

    #背景板
    normal_kmer_set=set()
    normal_bam = pysam.AlignmentFile(normal_bam_file, 'r')

    #如果变异很长，那么此步需要处理的reads数非常多，耗时
    normal_region_reads = normal_bam.fetch(contig=chro, start=ref_bk1 - 1000, end=ref_bk2 + 1000)
    for aln in normal_region_reads:
        if aln.is_unmapped or aln.mapping_quality < 20:
            continue
        else:
            seq = aln.query_sequence
            for i in range(0, len(seq) - k + 1):
                kmer = seq[i:i + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                normal_kmer_set.add(mkmer)
    normal_bam.close()

    ref_region=ref_dict[chro][ref_bk1-100:ref_bk2+100]
    for i in range(0, len(ref_region) - k + 1):
        kmer = ref_region[i:i + k]
        rkmer=get_reverse_comp(kmer)
        mkmer=rkmer if rkmer<kmer else kmer
        normal_kmer_set.add(mkmer)


    #获取跨过SV断点的k-mer

    somatic_kmer_set=dict()
    somatic_count_sum=0
    pos = list()
    radios=list()


    name2seq=dict()
    for aln in somatic_support_reads:
        if aln.query_name in name2seq.keys():
            continue
        else:
            if not aln.is_reverse:
                name2seq[aln.query_name]=aln.query_sequence
            else:
                # print(aln.query_sequence)
                name2seq[aln.query_name]=get_reverse_comp(aln.query_sequence)

    for i in range(len(bk[2])):
        pos.append(list())
        read_name = bk[2][i]
        read_sv_bk1=bk[3][i]
        read_sv_bk2=bk[4][i]
        query_sequence=name2seq[read_name]

        if sv_type=="INS":
            read_sv_bk1 = bk[4][i]
            read_sv_bk2 = bk[5][i]
        somatic_count = 0
        #对于deletion和duplication来说，最多会产生32个somatic k-mer
        if sv_type=='DEL' or sv_type=='DUP':
            # print(read_sv_bk1-k+1,read_sv_bk1+1)
            for j in range(read_sv_bk1-k+1,read_sv_bk1+1):
                kmer = query_sequence[j:j + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                if mkmer not in normal_kmer_set:
                    pos[-1].append(j)
                    if mkmer in somatic_kmer_set.keys():
                        somatic_kmer_set[mkmer]=somatic_kmer_set[mkmer]+1
                    else:
                        somatic_kmer_set[mkmer]=1
                    somatic_count_sum = somatic_count_sum + 1
                    somatic_count = somatic_count + 1
                # else:
                #     print("in ",j)
            radio=somatic_count/k
        #对于insertion和inversion来说，最多会产生64个somatic k-mer
        elif sv_type=='INS' or sv_type=='INV':
            for j in range(read_sv_bk1-k+1,read_sv_bk1+1):
                kmer = query_sequence[j:j + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                # print(rkmer)
                if mkmer not in normal_kmer_set:
                    # print("not in ",j)
                    # print(j,mkmer,mkmer)
                    pos[-1].append(j)
                    if mkmer in somatic_kmer_set.keys():
                        somatic_kmer_set[mkmer]=somatic_kmer_set[mkmer]+1
                    else:
                        somatic_kmer_set[mkmer]=1
                    somatic_count_sum = somatic_count_sum + 1
                    somatic_count = somatic_count + 1
                # else:
                #     print("in")
            # print("right")
            for j in range(read_sv_bk2-k,read_sv_bk2):
                kmer = query_sequence[j:j + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                # print(kmer,rkmer)
                if mkmer not in normal_kmer_set:
                    pos[-1].append(j)
                    if mkmer in somatic_kmer_set.keys():
                        somatic_kmer_set[mkmer]=somatic_kmer_set[mkmer]+1
                    else:
                        somatic_kmer_set[mkmer]=1
                    somatic_count_sum = somatic_count_sum + 1
                    somatic_count = somatic_count + 1
                # else:
                #     print("in")
            radio = somatic_count / (2*k)
        radios.append(radio)
    clusters=list()
    sum_cluster=0
    max_cluster_size=0
    for i in range(len(pos)):
        l=pos[i]
        clusters.append(list())
        if len(l)==0:
            continue
        else:
            tmp=list()
            tmp.append(l[0])
            for j in range(1,len(l)):
                if l[j]==l[j-1]+1:
                    tmp.append(l[j])
                else:
                    clusters[-1].append(tmp)
                    sum_cluster=sum_cluster+1
                    max_cluster_size=max(max_cluster_size,len(tmp))
                    tmp=list()
                    tmp.append(l[j])
            max_cluster_size = max(max_cluster_size, len(tmp))
            clusters[-1].append(tmp)
            sum_cluster = sum_cluster + 1

    if len(somatic_kmer_set)!=0:
        values=list(somatic_kmer_set.values())
        values.sort()
        #各somatic k-mer出现次数的中位数，如果是somatic sv的话，中位数/reads_count大约为1，如果不是，中位数/reads_count接近0
        medium=np.median(values)
    else:
        medium=0
    # somatic_kmer的种类，
    # somatic k-mer出现次数的中位数
    # somatic k-mer在sv区域的平均占比,
    # 平均每个reads包含的somatic kmer的数量,
    # 平均每个reads上clusters的数量,
    # 最大的cluster的大小
    return len(somatic_kmer_set),medium/len(bk[2]),np.mean(radios),somatic_count_sum/len(bk[2]),sum_cluster/len(bk[2]),max_cluster_size


