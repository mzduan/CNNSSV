if __name__ == '__main__':

    fout=open('/home/mzduan/somaticSV/COLO829_results/nanomonsv_results.vcf','w')
    for i in range(22,12,-1):
        fin=open('/home/mzduan/somaticSV/COLO829_results/chr'+str(i)+'/nanomonsv/tumor.nanomonsv.result.vcf','r')

        while True:
            l=fin.readline()
            if l:
                if l[0]!='#':
                    fout.write(l)
                else:
                    break
    fin.close()
    fout.close()
