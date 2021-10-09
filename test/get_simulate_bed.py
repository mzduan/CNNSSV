import re
import sys
if __name__ == '__main__':

    chro_digit=sys.argv[1]

    vcf=open('/Users/duan/Desktop/results/somaticSV/callset/gd/nstd152.GRCh38.variant_call.vcf','r')
    simulate_bed=open('/Users/duan/Desktop/results/somaticSV/callset/gd/DEL_nstd152.GRCh38.variant_call.NA19240.bed','w')

    chrom_bed=open('/Users/duan/Desktop/results/somaticSV/callset/gd/NA19240.chr' +chro_digit + '.bed','w')

    # chrom_set=set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22'])
    chrom_set=set([chro_digit])
    type_set=set()
    while True:
        l=vcf.readline()
        if l:
            infos=re.split('\s+',l)
            if infos[0][0]=='#':
                continue

            sups = infos[7]

            #求end_pos
            end_pos = sups.find(';END')
            end_pair = ""
            for k in range(end_pos + 1, len(sups)):
                if sups[k] != ';':
                    end_pair = end_pair + sups[k]
                else:
                    break
            end = end_pair.split('=')[1]

            #求sv_type
            type_pos = sups.find(';SVTYPE')
            type_pair = ""
            for k in range(type_pos + 1, len(sups)):
                if sups[k] != ';':
                    type_pair = type_pair + sups[k]
                else:
                    break
            sv_type = type_pair.split('=')[1]
            if sv_type=='CNV':
                continue

            ins_seq=""
            if sv_type=='INS': #求一下插入的序列
                seq_pos = sups.find(';SEQ')
                if seq_pos!=-1:
                    seq_pair = ""
                    for k in range(seq_pos + 1, len(sups)):
                        if sups[k] != ';' and sups[k]!='\n':
                            seq_pair = seq_pair + sups[k]
                        else:
                            break
                    ins_seq = seq_pair.split('=')[1]

            #求sample_info
            sample_pos = sups.find(';SAMPLE')
            sample_pair = ""
            for k in range(sample_pos + 1, len(sups)):
                if sups[k] != ';':
                    sample_pair = sample_pair + sups[k]
                else:
                    break
            sample = sample_pair.split('=')[1]
            if sample=='NA19240':

                #染色体号：
                chrom=infos[0]
                if str(chrom) in chrom_set:
                    if sv_type=='DEL':
                        simulate_bed.write(l)
                        type_set.add(sv_type)
                    if sv_type!='INS':
                        chrom_bed.write(str(chrom) + '\t' + str(infos[1]) + '\t' + str(end) + '\t' + sv_type + '\t' + 'None' + '\t' + '0\n')
                    else:
                        if ins_seq!="":
                            chrom_bed.write(str(chrom) + '\t' + str(infos[1]) + '\t' + str(int(end)+1) + '\t' + sv_type + '\t' + ins_seq + '\t' + '0\n')
        else:
            break

    vcf.close()
    simulate_bed.close()
    chrom_bed.close()
