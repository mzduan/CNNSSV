import re
import numpy as np
if __name__ == '__main__':

    sv_fin=open('/Users/duan/Desktop/string_features_lost.txt','r')
    gd_fin=open('/Users/duan/Desktop/getBreakpoint/groundtruth/simulate/chr20.somatic.bed','r')

    DEL_somatic=list()
    INS_somatic=list()
    INV_somatic=list()
    DUP_somatic=list()

    DEL_germline=list()
    INS_germline=list()
    INV_germline=list()
    DUP_germline=list()

    sv_candidates=list()
    while True:
        l=sv_fin.readline()
        if l:
            infos=re.split('\s+',l)
            chrom=infos[0]
            sv_start=int(infos[1])
            sv_len=int(infos[2])
            sv_type=infos[3]

            somatic_unique_kmer_count=int(infos[4])
            count_sum=int(infos[5])
            if sv_type=='INS':
                sv_end=sv_start+1
            else:
                sv_end=sv_start+sv_len
            sv_candidates.append((chrom,sv_start,sv_end,sv_type,somatic_unique_kmer_count,count_sum))
        else:
            break
    gd = list()
    while True:
        l = gd_fin.readline()
        if l:
            infos = re.split('\s+', l)
            chrom = infos[0]
            start = infos[1]
            end = infos[2]
            raw_sv_type=infos[3]
            if raw_sv_type == 'insertion':
                sv_type='INS'
            elif raw_sv_type == 'deletion':
                sv_type='DEL'
            elif raw_sv_type == 'inversion':
                sv_type='INV'
            elif raw_sv_type == 'tandem':
                sv_type='DUP'
            gd.append((chrom, int(start), int(end), sv_type))
        else:
            break

    for p in sv_candidates:
        find_flag=False
        for g in gd:
            if p[3]==g[3] and p[0]==g[0]:
                if abs(int(p[1])-int(g[1]))<=200 and abs(int(p[2])-int(g[2]))<=200:
                    find_flag=True
                    if p[3]=='DEL':
                        if p[5] != 0:
                            DEL_somatic.append(p[4]/p[5])
                    elif p[3]=='INS':
                        if p[5] != 0:
                            INS_somatic.append(p[4]/p[5])
                    elif p[3]=='INV':
                        if p[5] != 0:
                            INV_somatic.append(p[4]/p[5])
                    elif p[3]=='DUP':
                        if p[5] != 0:
                            DUP_somatic.append(p[4]/p[5])
                    break
        if not find_flag:
            if p[3] == 'DEL':
                if p[5]!=0:
                    DEL_germline.append(p[4]/p[5])
            elif p[3] == 'INS':
                if p[5] != 0:
                    INS_germline.append(p[4]/p[5])
            elif p[3] == 'INV':
                if p[5]!=0:
                    INV_germline.append(p[4]/p[5])
            elif p[3] == 'DUP':
                if p[5] != 0:
                    DUP_germline.append(p[4]/p[5])
    sv_fin.close()
    gd_fin.close()

    # for p in DEL_somatic:
    #     print(p)
    # for p in INS_somatic:
    #     print(p)
    # for p in INV_somatic:
    #     print(p)
    # for p in DUP_somatic:
    #     print(p)

    # print(np.mean(DEL_somatic)/32)
    # print(np.mean(INS_somatic)/64)
    # print(np.mean(INV_somatic)/64)
    # print(np.mean(DUP_somatic)/32)
    #
    # print(np.mean(DEL_germline)/32)
    # print(np.mean(INS_germline)/64)
    # print(np.mean(INV_germline)/64)
    # print(np.mean(DUP_germline)/32)


    print(np.mean(DEL_somatic))
    print(np.mean(INS_somatic))
    print(np.mean(INV_somatic))
    print(np.mean(DUP_somatic))

    print(np.mean(DEL_germline))
    print(np.mean(INS_germline))
    print(np.mean(INV_germline))
    print(np.mean(DUP_germline))
