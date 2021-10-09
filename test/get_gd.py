import re
#sed -i -e 's/^/chr/' NA19240.chr20.somatic.vcf
#grep '^20' NA19238.vcf > NA19238.chr20.vcf
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

    NA19239_vcf=open('/home/duan/Desktop/somaticSV/groundtruth/NA19239.chr20.vcf','r')
    NA19240_vcf = open('/home/duan/Desktop/somaticSV/groundtruth/NA19240.chr20.vcf', 'r')

    NA19239_readlines=list()
    NA19240_readlines=list()

    while True:
        l=NA19239_vcf.readline()
        if l:
            NA19239_readlines.append(l)
        else:
            break

    while True:
        l=NA19240_vcf.readline()
        if l:
            NA19240_readlines.append(l)
        else:
            break


    NA19240_somatic=open('/home/duan/Desktop/somaticSV/groundtruth/NA19240.chr20.somatic.vcf', 'w')

    used_pair=dict()
    for i in NA19240_readlines:
        i_infos=re.split('\s+',i)

        i_sv_type=i_infos[4][1:4]
        i_sv_start=int(i_infos[1])
        i_sups=i_infos[7]
        i_kv=getKV(i_sups)

        if 'SVLEN' not in i_kv.keys():
            continue
        i_sv_len=i_kv['SVLEN']
        i_sv_len=abs(int(i_sv_len))

        i_sv_end=i_sv_start+i_sv_len


        find_flag=False
        for j in NA19239_readlines:
            j_infos = re.split('\s+', j)

            j_sv_type = j_infos[4][1:4]
            j_sv_start = int(j_infos[1])
            j_sups = j_infos[7]

            j_kv = getKV(j_sups)

            if 'SVLEN' not in j_kv.keys():
                continue
            j_sv_len = j_kv['SVLEN']
            j_sv_len = abs(int(j_sv_len))

            j_sv_end = j_sv_start+j_sv_len

            if i_sv_type==j_sv_type and abs(i_sv_start-j_sv_start)<=100 and abs(i_sv_end-j_sv_end) <=100 :
                find_flag=True
                if j in used_pair:
                    used_pair[j].append(i)
                else:
                    used_pair[j]=[i]
                # if abs(i_sv_len-j_sv_len)>100:
                #     print(i_sv_type,i_sv_start,i_sv_end,i_sv_len,j_sv_start,j_sv_end,j_sv_len)
        if not find_flag:
            NA19240_somatic.write(i)

    NA19239_vcf.close()
    NA19240_vcf.close()
    NA19240_somatic.close()
    for k in used_pair:
        if len(used_pair[k])>1:
            print(k,used_pair[k])