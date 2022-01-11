import re
import numpy as np
import os
if __name__ == '__main__':

    del_bed=open('/Users/duan/Downloads/文档/论文/somatic_SV/cuteSV/cuteSV-master/simulation/sim_inv.bed','r')
    sv_dict=dict()
    while True:
        l=del_bed.readline()
        if l:
            infos=re.split('\s+',l)
            chrom=infos[0]
            if chrom in sv_dict.keys():
                sv_dict[chrom].append(l)
            else:
                sv_dict[chrom]=list()
                sv_dict[chrom].append(l)
        else:
            break
    for i in range(1,23,1):
        chrom=str(i)
        if chrom in sv_dict.keys():
            sv_list=sv_dict[chrom]

            pos_range = range(0, len(sv_list))

            half = len(sv_list) / 2
            half = int(half)

            pos_sample = np.random.choice(pos_range, half, replace=False)

            wkdir='/Users/duan/Downloads/文档/论文/somatic_SV/cuteSV/cuteSV-master/simulation/chr'+chrom
            # os.mkdir(wkdir)

            tumor_fout=open(wkdir+'/chr_'+chrom+'_tumor.bed','a')
            normal_fout = open(wkdir+'/chr_' + chrom + '_normal.bed', 'a')
            somatic_fout = open(wkdir+'/chr_' + chrom + '_somatic.bed', 'a')

            for j in range(len(sv_list)):
                tumor_fout.write(sv_list[j])
                if j in pos_sample:
                    normal_fout.write(sv_list[j])
                else:
                    somatic_fout.write(sv_list[j])

            tumor_fout.close()
            normal_fout.close()
            somatic_fout.close()
    del_bed.close()