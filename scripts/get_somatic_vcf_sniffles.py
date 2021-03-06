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



    tags = ['500', '2000','2500']
    for t in tags:
    # for t in range(1,23,1):
        tumor_vcf=open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_tumor_'+t+'.vcf','r')
        normal_vcf = open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_normal_'+t+'.vcf','r')
        somatic_vcf = open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_somatic_'+t+'.vcf', 'w')


        tumor_readlines=list()
        normal_readlines=list()

        while True:
            l=tumor_vcf.readline()
            if l:
                if l[0]!='#':
                    infos = re.split('\s+', l)
                    sups=infos[7]

                    tumor_kv=getKV(sups)
                    if 'SVTYPE' not in tumor_kv.keys():
                        continue
                    else:
                        sv_type=tumor_kv['SVTYPE']
                        if sv_type in ["INS", "INV", "DEL", "DUP"]:
                            tumor_readlines.append(l)
            else:
                break

        while True:
            l=normal_vcf.readline()
            if l:
                if l[0] != '#':
                    infos = re.split('\s+', l)
                    sups=infos[7]

                    normal_kv=getKV(sups)
                    if 'SVTYPE' not in normal_kv.keys():
                        continue
                    else:
                        sv_type=normal_kv['SVTYPE']
                        if sv_type in ["INS", "INV", "DEL", "DUP"]:
                            normal_readlines.append(l)
            else:
                break


        for i in tumor_readlines:

            i_infos=re.split('\s+',i)
            i_sv_start=int(i_infos[1])
            i_sups=i_infos[7]

            tumor_kv = getKV(i_sups)
            i_sv_type = tumor_kv['SVTYPE']
            if 'SVLEN' not in tumor_kv.keys():
                continue
            else:
                i_sv_len=abs(int(tumor_kv['SVLEN']))

            if i_sv_len<30:
                continue


            i_sv_end=i_sv_start+i_sv_len

            find_flag=False
            for j in normal_readlines:
                j_infos = re.split('\s+', j)
                j_sv_start = int(j_infos[1])

                j_sups = j_infos[7]

                normal_kv = getKV(j_sups)
                j_sv_type = normal_kv['SVTYPE']
                if 'SVLEN' not in normal_kv.keys():
                    continue
                else:
                    j_sv_len = abs(int(normal_kv['SVLEN']))
                    if j_sv_len<30:
                        continue
                j_sv_end = j_sv_start + j_sv_len

                if i_sv_type==j_sv_type and abs(i_sv_start-j_sv_start)<=100 and abs(i_sv_end-j_sv_end) <=100:
                    find_flag=True

            if not find_flag:
                somatic_vcf.write(i)

        tumor_vcf.close()
        normal_vcf.close()
        somatic_vcf.close()
