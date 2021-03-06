
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
        else:
            ret=ret+'N'
    return ret

def get_unique_kmer_radio_in_normal(aln, left, right, k, tumor_kmer_set):
    # print(aln.query_name)
    left_lost_count  = 0
    right_lost_count = 0

    overlap_left=False
    overlap_right=False
    base_cigar = ""
    for i in range(len(aln.cigartuples)):
        if aln.cigartuples[i][0] == 0:
            base_cigar = base_cigar + aln.cigartuples[i][1] * 'M'
        elif aln.cigartuples[i][0] == 1:
            base_cigar = base_cigar + aln.cigartuples[i][1] * 'I'
        elif aln.cigartuples[i][0] == 2:
            base_cigar = base_cigar + aln.cigartuples[i][1] * 'D'
        elif aln.cigartuples[i][0] == 4:
            base_cigar = base_cigar + aln.cigartuples[i][1] * 'S'

    query_pos = 0
    ref_pos = aln.reference_start

    left_bk_in_query=0
    right_bk_in_query=0

    for i in range(len(base_cigar)):
        c = base_cigar[i]
        if c == 'S':
            query_pos = query_pos + 1
        elif c == 'I':
            query_pos = query_pos + 1
        elif c == 'D':
            ref_pos = ref_pos + 1
        elif c == 'M':
            ref_pos = ref_pos + 1
            query_pos = query_pos + 1
        if ref_pos == left:
            if not overlap_left:
                overlap_left=True
                left_bk_in_query=query_pos
        elif ref_pos == right:
            if not overlap_right:
                overlap_right=True
                right_bk_in_query=query_pos
        elif ref_pos > right:
            break

    if overlap_left:
        for j in range(left_bk_in_query - k + 1, left_bk_in_query + 1):
            kmer = aln.query_sequence[j:j + k]
            if len(kmer) < k:
                continue
            rkmer = get_reverse_comp(kmer)
            mkmer = rkmer if rkmer < kmer else kmer
            if mkmer not in tumor_kmer_set:
                left_lost_count = left_lost_count + 1
    if overlap_right:
        for j in range(right_bk_in_query- k + 1, right_bk_in_query + 1):
            kmer = aln.query_sequence[j:j + k]
            if len(kmer) < k:
                continue
            rkmer = get_reverse_comp(kmer)
            mkmer = rkmer if rkmer < kmer else kmer
            if mkmer not in tumor_kmer_set:
                right_lost_count = right_lost_count + 1

    return left_lost_count/k,right_lost_count/k,overlap_left,overlap_right

def get_somatic_kmer(sv_type,somatic_support_reads,tumor_bam_file,normal_bam_file,ref_dict,chro,bk,kmer_size):

    ref_bk1=bk[0]
    ref_bk2=bk[0]+bk[1]
    if sv_type=="INS":
        ref_bk2=ref_bk1+1

    # k=31
    k=kmer_size
    #背景板
    normal_kmer_set=set()
    normal_bam = pysam.AlignmentFile(normal_bam_file, 'r')
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
        # uncertain_list.append(list())
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
            radio=somatic_count/k
        #对于insertion和inversion来说，最多会产生64个somatic k-mer
        elif sv_type=='INS' or sv_type=='INV':
            for j in range(read_sv_bk1-k+1,read_sv_bk1+1):
                kmer = query_sequence[j:j + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                # print(rkmer)
                if mkmer not in normal_kmer_set:
                    pos[-1].append(j)
                    if mkmer in somatic_kmer_set.keys():
                        somatic_kmer_set[mkmer]=somatic_kmer_set[mkmer]+1
                    else:
                        somatic_kmer_set[mkmer]=1
                    somatic_count_sum = somatic_count_sum + 1
                    somatic_count = somatic_count + 1
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
            radio = somatic_count / (2*k)
        radios.append(radio)

    #获取normal样本中，跨过sv断点的kmer
    #   deletion在read上有一个断点，在ref上有两个断点
    #   insertion在read上有两个断点，在ref上有一个断点
    #   dup在read上有一个断点,在ref上有两个断点
    #   inv在read上有两个断点，在ref上有两个断点

    #先构建tumor的背景板
    normal_left_radios=list()
    normal_right_radios = list()
    tumor_support_reads_kmers=set()
    tumor_bam = pysam.AlignmentFile(tumor_bam_file, 'r')
    tumor_region_reads = tumor_bam.fetch(contig=chro, start=ref_bk1 - 1000, end=ref_bk2 + 1000)
    for aln in tumor_region_reads:
        if aln.query_name in set(bk[2]):
            seq = aln.query_sequence
            for i in range(0, len(seq) - k + 1):
                kmer = seq[i:i + k]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                tumor_support_reads_kmers.add(mkmer)
    tumor_bam.close()

    normal_bam = pysam.AlignmentFile(normal_bam_file, 'r')
    normal_region_reads = normal_bam.fetch(contig=chro, start=ref_bk1 - 1000, end=ref_bk2 + 1000)

    for aln in normal_region_reads:
        if aln.reference_end > ref_bk1 and aln.reference_start < ref_bk2:
            tmp_lost_count=0
            tmp_k=0
            normal_left_radio,normal_right_radio,overlap_left,overlap_right=get_unique_kmer_radio_in_normal(aln, ref_bk1, ref_bk2, k, tumor_support_reads_kmers)
            if overlap_left:
                tmp_lost_count+=int(normal_left_radio*k)
                tmp_k+=k
                normal_left_radios.append(normal_left_radio)
            if overlap_right:
                tmp_lost_count+= int(normal_right_radio * k)
                tmp_k+=k
                normal_right_radios.append(normal_right_radio)
    normal_bam.close()

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
    # normal中断点附近的k-mer在somatic sv support reads中出现的次数的最小值和最大值
    # 平均每个reads包含的somatic kmer的数量,
    # 平均每个reads上clusters的数量,
    # 最大的cluster的大小
    # 断点附近的凌乱程度（新增）
    # print(normal_left_radios)
    # print(normal_right_radios)
    # print(np.mean(radios),min(normal_left_radios),max(normal_left_radios),np.mean(normal_left_radios),\
    #       min(normal_right_radios),max(normal_right_radios),np.mean(normal_right_radios))

    return len(somatic_kmer_set),medium/len(bk[2]),np.mean(radios),min(normal_left_radios),max(normal_left_radios),\
           np.mean(normal_left_radios),min(normal_right_radios),max(normal_right_radios),\
           np.mean(normal_right_radios),somatic_count_sum/len(bk[2]),sum_cluster/len(bk[2]),max_cluster_size


