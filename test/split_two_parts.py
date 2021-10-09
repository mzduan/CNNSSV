import re
import numpy as np
import sys
if __name__ == '__main__':


    sv_file_name=sys.argv[1]
    work_dir=sys.argv[2]
    chrom=sys.argv[3]


    sv_file=open(sv_file_name,'r')


    INS_list=list()
    DEL_list=list()
    INV_list=list()
    TUP_list=list()


    germline_list=list()
    somatic_list=list()

    while True:
        line=sv_file.readline()
        if line:
            sv_type=re.split('\s+',line)[3]
            if sv_type=='insertion':
                INS_list.append(line)
            elif sv_type=='tandem':
                TUP_list.append(line)
            elif sv_type=='inversion':
                INV_list.append(line)
            elif sv_type=='deletion':
                DEL_list.append(line)
        else:
            break

    pos_range=range(0,len(INS_list))

    half=len(INS_list)/2
    half=int(half)

    pos_sample=np.random.choice(pos_range,half,replace=False)


    for i in range(len(INS_list)):
        if i in pos_sample:
            germline_list.append(INS_list[i])
            germline_list.append(INV_list[i])
            germline_list.append(TUP_list[i])
            germline_list.append(DEL_list[i])
        else:
            somatic_list.append(INS_list[i])
            somatic_list.append(INV_list[i])
            somatic_list.append(TUP_list[i])
            somatic_list.append(DEL_list[i])

    with open(work_dir+chrom+'.germline.bed','w') as fout:
        for l in germline_list:
            fout.write(l)

    with open(work_dir+chrom+'.somatic.bed','w') as fout:
        for l in somatic_list:
            fout.write(l)




    sv_file.close()
