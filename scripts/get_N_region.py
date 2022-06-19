from Bio import SeqIO
import sys
if __name__ == '__main__':


    fa_file=sys.argv[1]
    fout_file=sys.argv[2]
    chrom=sys.argv[3]

    records = list(SeqIO.parse(fa_file, "fasta"))

    fout=open(fout_file,'w')


    ref_seq_dict = {}
    for record in records:
        chrom = record.id
        ref_seq_dict[chrom] = record.seq

    seq=ref_seq_dict[chrom]
    N_region=list()

    start_pos=list()
    start_pos.append(0)
    end_pos=list()

    for i in range(1,len(seq)-1):
        if seq[i]=='N':
            if seq[i-1]!='N':
                start_pos.append(i)
            if seq[i+1]!='N':
                end_pos.append(i)

    end_pos.append(len(seq))

    for i in range(len(start_pos)):
        if end_pos[i]-start_pos[i]>50:
            N_region.append((start_pos[i],end_pos[i]))

    for region in N_region:
        fout.write(chrom+'\t'+str(region[0])+'\t'+str(region[1])+'\n')

    fout.close()