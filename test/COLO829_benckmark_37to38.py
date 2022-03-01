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
    fin=open('/Users/duan/Desktop/truthset_somaticSVs_COLO829.vcf','r')
    fout=open('/Users/duan/Desktop/lifover_input.bed','w')


    flag=True
    while True:
        l=fin.readline()
        if l:
            if l[0]=='#':
                continue
            else:
                infos=re.split('\s+',l)

                if infos[0]=='X':
                    continue
                chrom=int(infos[0])
                sv_start=int(infos[1])
                kvs=getKV(infos[7])

                sv_type=kvs['SVTYPE']
                if sv_type=='BND':
                    continue
                else:
                    sv_len=int(kvs['SVLEN'])
                    if sv_type=='INS':
                        sv_end=sv_start+1
                    else:
                        sv_end=sv_start+sv_len
                    if flag:
                        fout.write('chr'+str(chrom)+'\t'+str(sv_start)+'\t'+str(sv_end)+'\t'+sv_type+'\t'+str(sv_len)+'\n')
                        if sv_type=='INS':
                            flag=True
                        else:
                            flag=False
                    else:
                        flag=True

        else:
            break


    fin.close()
    fout.close()
