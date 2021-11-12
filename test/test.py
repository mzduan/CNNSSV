import pysam
if __name__ == '__main__':
    bam=pysam.AlignmentFile('/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/NA19239.chr20.bam','rb')
    for aln in bam:
        if aln.query_name=='m64039_190910_140737/179440323/ccs' and aln.reference_start==24400773:
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
                if query_pos==7888:
                    print(ref_pos)
            break


    bam.close()


