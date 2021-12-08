import pysam
import cigar
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
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/home/duan/Desktop/somaticSV/bam/CCS/0.7/somatic_bam_chr20/sim.srt.bam','r')
    for aln in bam:
        if aln.query_name=='C2_H1_25202':
            print(aln.query_sequence)
            reversed=get_reverse_comp(aln.query_sequence)
            print(len(aln.query_sequence))
            print(len(reversed))


    bam.close()
