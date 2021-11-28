import re
if __name__ == '__main__':

    somatic_vcf = open('/Users/duan/Desktop/getBreakpoint/results/mixed/nanomonsv/0.7.tumor.nanomonsv.result.vcf', 'r')
    somatic_bed = open('/Users/duan/Desktop/getBreakpoint/results/mixed/nanomonsv/0.7.tumor.nanomonsv.result.bed', 'w')

    while True:
        l=somatic_vcf.readline()
        if l:
            infos=re.split('\s+',l)
            if infos[0][0]=='#':
                continue
            chr=infos[0]
            start=infos[1]

            sups = infos[7]

            #求sv_type
            type_pos = sups.find(';SVTYPE')
            type_pair = ""
            for k in range(type_pos + 1, len(sups)):
                if sups[k] != ';':
                    type_pair = type_pair + sups[k]
                else:
                    break
            sv_type = type_pair.split('=')[1]

            if sv_type=='BND':
                continue


            #求end坐标
            end_pos = sups.find('END')
            end_pair = ""
            for k in range(end_pos, len(sups)):
                if sups[k] != ';':
                    end_pair = end_pair + sups[k]
                else:
                    break
            sv_end = end_pair.split('=')[1]
            sv_end = abs(int(sv_end))


            #求sv_len

            len_pos = sups.find(';SVLEN')
            len_pair = ""
            for k in range(len_pos + 1, len(sups)):
                if sups[k] != ';':
                    len_pair = len_pair + sups[k]
                else:
                    break
            sv_len = len_pair.split('=')[1]
            sv_len = abs(int(sv_len))

            somatic_bed.write(chr+'\t'+str(start)+'\t'+str(sv_end)+'\t'+sv_type+'\t'+str(sv_len)+'\n')

        else:
            break


    somatic_vcf.close()
    somatic_bed.close()