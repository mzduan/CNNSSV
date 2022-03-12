import re
if __name__ == '__main__':
    fout='/data/home/wlzhang/somaticSV/COLO829_results/nanomonsv/minimap2'
    for t in range(1,23,1):
        fin=open('/data/home/wlzhang/somaticSV/COLO829_results/nanomonsv/minimap2/chr'+str(t)+'/tumor.nanomonsv.result.vcf')
        while True:
            l=fin.readline()
            if l:
                infos=re.split('\s+',l)
                if infos[0]=='#':
                    continue
                else:
                    fout.write(l)
            else:
                break
        fin.close()
    fout.close()