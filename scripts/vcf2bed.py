import re
def getKV(str):
    ret=dict()
    splits=re.split(';',str)
    for kv in splits:
        infos=re.split('=',kv)
        if len(infos)==2:
            key=re.split('=',kv)[0]
            value=re.split('=',kv)[1]
            ret[key]=value
    return ret
if __name__ == '__main__':

    # tags=['0.3']
    # tags=['1','2','3','4','5','6']
    # for t in tags:
    tags = ['500', '2000','2500']
    for t in tags:
        somatic_vcf = open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_somatic_'+t+'.vcf', 'r')
        somatic_bed = open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_somatic_'+t+'.bed', 'w')

        while True:
            l=somatic_vcf.readline()
            if l:
                infos=re.split('\s+',l)
                if infos[0][0]=='#':
                    continue
                sv_chr=infos[0]
                sv_start=int(infos[1])

                sups = infos[7]
                #求sv_type
                kv = getKV(sups)

                if 'SVLEN' not in kv.keys() or 'SVTYPE' not in kv.keys():
                    continue
                sv_len = kv['SVLEN']
                sv_len = abs(int(sv_len))

                sv_type=kv['SVTYPE']

                if 'END' in kv.keys():
                    sv_end = int(kv['END'])
                else:
                    sv_end = sv_start+1
                if sv_type=='INS':
                    sv_end=sv_start+1

                # print("before")
                somatic_bed.write(sv_chr+'\t'+str(sv_start)+'\t'+str(sv_end)+'\t'+sv_type+'\t'+str(sv_len)+'\n')
                # print("after")

            else:
                break


        somatic_vcf.close()
        somatic_bed.close()