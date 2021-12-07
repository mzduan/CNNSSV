import pysam
import cigar
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/home/duan/Desktop/somaticSV/bam/CCS/0.7/somatic_bam_chr20/sim.srt.bam','r')
    for aln in bam:
        # if aln.has_tag("SA"):
        if aln.query_name=='C2_H1_48011':
            # print(aln.query_name,aln.reference_start,aln.cigarstring)
            sa_tag = aln.get_tag("SA").split(";")
            print(sa_tag)
            MD_tag=aln.get_tag("MD").split(";")
            print(MD_tag)
            # for sup_aln in sa_tag:
            #     fields = sup_aln.split(",")
            #     if len(fields) != 6:
            #         continue
            #     local_chr = fields[0]
            #     local_start = int(fields[1]) - 1
            #     local_cigar = fields[3]
            #     local_strand = fields[2]
            #     local_mapq = int(fields[4])
            #     print(aln.query_name,local_start)
            #     if local_strand=='-':
            #         c = list(cigar.Cigar(local_cigar).items())
            #         print(local_cigar,"  ",c)
            #     else:
            #         print(local_cigar)

    bam.close()
