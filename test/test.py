import pysam
import cigar
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/home/duan/Downloads/0.2.chr18.tumor.bam','rb')
    for aln in bam:
        if aln.query_name=='C1_H1_17895':
            print(aln.reference_start,aln.reference_end,aln.get_tag("SA"))

    bam.close()


