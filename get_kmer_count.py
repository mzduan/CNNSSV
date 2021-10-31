
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

    ref_bk1=bk[0]
    ref_bk2=bk[0]+bk[1]
    if sv_type=="INS":
        ref_bk2=ref_bk1+1
    kmer_len=31
    #先找出跨过 tumor sv断点的 kmer
    tumor_sv_kmer=dict()
    for i in range(len(bk[2])):
        read_name = bk[2][i]
        query_sequence=name2seq[read_name]
        if sv_type=="INS":
            read_sv_bk1 = bk[4][i]
            read_sv_bk2 = bk[5][i]
        else:
            read_sv_bk1 = bk[3][i]
            read_sv_bk2 = bk[4][i]

        if sv_type == 'INS' or sv_type == 'INV':
            for j in range(read_sv_bk1 - kmer_len + 1, read_sv_bk1 + 1):
                kmer = query_sequence[j:j + kmer_len]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer

                if mkmer not in tumor_sv_kmer.keys():
                    tumor_sv_kmer[mkmer] = 1
                else:
                    tumor_sv_kmer[mkmer] +=1
            for j in range(read_sv_bk2 - kmer_len, read_sv_bk2):
                kmer = query_sequence[j:j + kmer_len]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                if mkmer not in tumor_sv_kmer.keys():
                    tumor_sv_kmer[mkmer] = 1
                else:
                    tumor_sv_kmer[mkmer] +=1
        elif sv_type=='DEL' or sv_type=='DUP': #只有一个断点
            for j in range(read_sv_bk1-kmer_len-15,read_sv_bk1+16):  #k+31
                kmer = query_sequence[j:j + kmer_len]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                # print(kmer,rkmer)
                if mkmer not in tumor_sv_kmer.keys():
                    tumor_sv_kmer[mkmer] = 1
                else:
                    tumor_sv_kmer[mkmer] +=1

    #按出现次数排序，选出出现次数最高的62个k-mer，作为somatic k-mer

    sorted(tumor_sv_kmer.items(), key=lambda item: item[1], reverse=True)

    somatic_kmer=dict()  #key->(t_counts,n_counts)
    count=0
    for k in tumor_sv_kmer.keys():
        somatic_kmer[k]=[tumor_sv_kmer[k],0]
        count=count+1
        if count==62:
            break

    #计算somatic_kmers在normal样本中出现的次数


    normal_bam = pysam.AlignmentFile(normal_bam_file, 'r')
    normal_region_reads = normal_bam.fetch(contig=chro, start=ref_bk1 - 1000, end=ref_bk2 + 1000)
    for aln in normal_region_reads:
        if aln.is_unmapped or aln.mapping_quality < 20:
            continue
        else:
            seq = aln.query_sequence
            for i in range(0, len(seq) - kmer_len + 1):
                kmer = seq[i:i + kmer_len]
                rkmer = get_reverse_comp(kmer)
                mkmer = rkmer if rkmer < kmer else kmer
                if mkmer in somatic_kmer.keys():
                    somatic_kmer[mkmer][1]=somatic_kmer[mkmer][1]+1
    normal_bam.close()

    sorted(somatic_kmer.items(), key=lambda item: item[1][0], reverse=True)


    tumor_vector=list()
    normal_vector=list()
    for k in somatic_kmer.keys():
        tumor_vector.append(somatic_kmer[k][0])
        normal_vector.append(somatic_kmer[k][1])
    if len(somatic_kmer)<62:
        for i in range(62-len(somatic_kmer)):
            tumor_vector.append(0)
            normal_vector.append(0)

    t_min=min(tumor_vector)
    t_max=max(tumor_vector)
    n_min=min(normal_vector)
    n_max=max(normal_vector)
    min_count=t_min if t_min<n_min else n_min
    max_count=t_max if t_max>n_max else n_max

    if min_count==max_count:
        for i in range(len(tumor_vector)):
            tumor_vector[i]=1
            normal_vector[i]=1
    else:
        for i in range(len(tumor_vector)):
            tumor_vector[i]=(tumor_vector[i]-min_count)/(max_count-min_count)
            normal_vector[i] = (normal_vector[i] - min_count) / (max_count - min_count)
    return np.array(tumor_vector,dtype=np.int16),np.array(normal_vector,dtype=np.int16)


