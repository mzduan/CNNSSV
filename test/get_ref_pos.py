import pysam
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
def get_ref_pos(aln,pos):

    #有重叠
    # if aln.query_alignment_end>pos and aln.query_alignment_start<pos:

    lost_count=0
    kmer_sum=0
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


    query_pos=0
    ref_pos=aln.reference_start
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
        if query_pos==pos:
            print(ref_pos)
    #     if ref_pos==right:
    #         for j in range(query_pos - k + 1, query_pos + 1):
    #             kmer = aln.query_sequence[j:j + k]
    #             rkmer = get_reverse_comp(kmer)
    #             mkmer = rkmer if rkmer < kmer else kmer
    #             if mkmer not in tumor_kmer_set:
    #                 lost_count = lost_count + 1
    #         kmer_sum += k
    #     if ref_pos>right:
    #         break
    # return lost_count/kmer_sum



if __name__ == '__main__':
    file_name='/home/duan/Desktop/somaticSV/bam/NA19238_NA19239_mixed/0.7.mixed.chr20.bam'
    bam=pysam.AlignmentFile(file_name,'r')
    for aln in bam:
        if aln.query_name=='m64039_190911_201425/35456717/ccs':
            get_ref_pos(aln,710)
            # print(aln.query_sequence)
    bam.close()
