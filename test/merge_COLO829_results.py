import re
if __name__ == '__main__':
    fout=open('/data/home/wlzhang/somaticSV/COLO829_results/cutesv/ngmlr/COLO829_ngmlr_cutesv.vcf','w')
    for t in range(1,23,1):
        fin=open('/data/home/wlzhang/somaticSV/COLO829_results/cutesv/ngmlr/cutesv_ngmlr_somatic_chr'+str(t)+'.vcf')
        while True:
            l=fin.readline()
            if l:
                infos=re.split('\s+',l)
                if infos[0][0]=='#':
                    continue
                else:
                    fout.write(l)
            else:
                break
        fin.close()
    fout.close()
