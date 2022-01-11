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
    benchmark=open('/Users/duan/Desktop/truthset_somaticSVs_COLO829_chr20.vcf','r')
    fout=open('/Users/duan/Desktop/truthset_somaticSVs_COLO829_chr20.bed','w')
    count=0
    row=0
    while True:
        l=benchmark.readline()
        if l:
            if row%2==0:
                splits=re.split('\s+',l)
                chrom=splits[0]
                if chrom[0]!='#':
                    # if chrom=='19' or chrom=='20' or chrom=='21' or chrom=='22':
                    if chrom == '20':
                        sups = splits[7]
                        kvs = getKV(sups)
                        if 'SVTYPE' in kvs.keys():
                            sv_type=kvs['SVTYPE']
                            if sv_type=='DEL' or sv_type=='INS' or sv_type=='DUP' or sv_type=='INV':
                                chrom=splits[0]
                                sv_start=int(splits[1])
                                sv_len=int(kvs['SVLEN'])
                                if sv_type=='INS':
                                    sv_end=sv_start+1
                                else:
                                    sv_end=sv_start+sv_len
                                fout.write(chrom+'\t'+str(sv_start)+'\t'+str(sv_end)+'\n')
            row=row+1
        else:
            break

    benchmark.close()
    fout.close()