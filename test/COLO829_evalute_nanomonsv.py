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

    fin=open('/Users/duan/Desktop/nanomonsv_results.vcf','r')
    nanomonsv_callset=set()
    while True:
        l=fin.readline()
        if l:
            if l[0]=='#':
                continue
            else:
                infos=re.split('\s+',l)

                chrom=infos[0]
                sv_start=int(infos[1])
                kvs=getKV(infos[7])

                sv_type=kvs['SVTYPE']
                if sv_type=='BND':
                    continue
                else:
                    if sv_type=='INS':
                        sv_end=sv_start+1
                        sv_len = int(kvs['SVINSLEN'])
                    else:
                        sv_end=sv_start+sv_len
                        sv_len = int(kvs['SVLEN'])
                    nanomonsv_callset.add((str(chrom),sv_start,sv_end,sv_type,sv_len))
        else:
            break
    gd=open('/Users/duan/Desktop/COLO829_benchmark_GRCh38_chr22_chr13.bed','r')
    gd_set=set()
    while True:
        l=gd.readline()
        if l:
            infos=re.split('\s+',l)
            chrom=infos[0]
            sv_start=int(infos[1])
            sv_end=int(infos[2])
            sv_type=infos[3]
            sv_len=int(infos[4])
            gd_set.add((str(chrom), sv_start, sv_end, sv_type, sv_len))
        else:
            break

    tp_count=0
    for k in nanomonsv_callset:
        for v in gd_set:
            if k[0]==v[0] and k[3]==v[3]:
                if abs(k[1]-v[1])<=100 and abs(k[4]-v[4])<=100:
                    tp_count+=1
    tb_count=0
    for k in gd_set:
        for v in nanomonsv_callset:
            if k[0]==v[0] and k[3]==v[3]:
                if abs(k[1]-v[1])<=100 and abs(k[4]-v[4])<=100:
                    tb_count+=1

    print("精确率：",tp_count/len(nanomonsv_callset))
    print("召回率：",tb_count/len(gd_set))

    print(len(gd_set))