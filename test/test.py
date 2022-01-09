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
    bed=open('/Users/duan/Desktop/truthset_somaticSVs_COLO829.vcf','r')
    count=0
    del_count=0
    ins_count=0
    inv_count=0
    dup_count=0
    while True:
        l=bed.readline()
        if l:
            splits=re.split('\s+',l)
            chrom=splits[0]
            if chrom[0]!='#':
                sups=splits[7]
                kvs=getKV(sups)
                if 'SVTYPE' in kvs.keys():
                    sv_type=kvs['SVTYPE']
                    if sv_type=='DEL':
                        del_count+=1
                    elif sv_type=='INS':
                        ins_count+=1
                    elif sv_type=='DUP':
                        dup_count+=1
                    elif sv_type=='INV':
                        inv_count+=1
        else:
            break

    bed.close()
    print("DEL:\t",del_count)
    print("INS:\t", ins_count)
    print("INV:\t", inv_count)
    print("DUP:\t", dup_count)