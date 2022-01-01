import pysam
if __name__ == '__main__':


    bam=pysam.AlignmentFile('/Users/duan/Downloads/COLO829_normal_chr20.bam','r')

    for aln in bam:
        print(aln.reference_name,aln.reference_start,aln.reference_end,aln.query_name)
    bam.close()