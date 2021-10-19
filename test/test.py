import pysam
import cigar
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/mixed.chr20.bam','rb')
    for aln in bam:
        if aln.query_name=='m54336U_190829_230546/120719613/ccs':
            query_pos = 0
            ref_pos = aln.reference_start
            # bias=0
            # for t in aln.cigartuples:
            #     flag = t[0]
            #     counts = t[1]
            #     if flag == 0:
            #         ref_pos = ref_pos + counts
            #         query_pos = query_pos + counts
            #     elif flag == 4:
            #         query_pos = query_pos + counts
            #     elif flag == 1:
            #         query_pos = query_pos + counts
            #     elif flag == 2:
            #         ref_pos = ref_pos + counts
            #     elif flag == 7:
            #         print("go")
            #     elif flag == 8:
            #         print("go")
            # print(aln.reference_start,aln.reference_end,ref_pos)

            seq = list(cigar.Cigar(aln.cigarstring).items())
            bias = 0
            for i in seq:
                if i[1]=='M':
                    ref_pos=ref_pos+i[0]
                    bias +=i[0]
                elif i[1]=='S':
                    query_pos=query_pos+i[0]
                elif i[1]=='I':
                    query_pos=query_pos+i[0]
                elif i[1]=='D':
                    ref_pos=ref_pos+i[0]
                    bias += i[0]
            print(bias)
            print(aln.reference_start,ref_pos)
            print("=========================")
    bam.close()


