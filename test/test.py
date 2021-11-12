import pysam
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/Users/duan/Downloads/bam/NA19239_NA19240_mixed/NA19239.chr20.bam','rb')
    for aln in bam:
        if aln.query_name=='m54336U_191005_142313/73074350/ccs' and aln.reference_start==14054367:
            peer_base_cigar=""
            for t in aln.cigartuples:
                flag = t[0]
                counts = t[1]
                peer_base_cigar=peer_base_cigar+counts*str(flag)

            query_pos=0
            ref_pos=aln.reference_start
            for m in peer_base_cigar:
                if m=='1' or m=='4':
                    query_pos=query_pos+1
                elif m=='0':
                    query_pos=query_pos+1
                    ref_pos=ref_pos+1
                elif m=='2':
                    ref_pos=ref_pos+1
                if query_pos==18110:
                    print(ref_pos)
            break


    bam.close()


