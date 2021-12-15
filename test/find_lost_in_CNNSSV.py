import re
if __name__ == '__main__':
    cutesv_kv=open('/home/duan/Desktop/cutesv.somatic7.kv','r')
    CNNSSV_fnb=open('/home/duan/Desktop/CNNSSV.somatic7.lost.txt','r')
    CNNSSV_candidate=open('/home/duan/Desktop/test/tumor.candidate.bed','r')

    fout=open('/home/duan/Desktop/CNNSSV.somatic7.fnc','w')

    fnb_set=set()
    while True:
        l=CNNSSV_fnb.readline()
        if l:
            fnb_set.add(l)
        else:
            break
    CNNSSV_fnb.close()

    sv_in_cutesv=list()
    while True:
        l1=cutesv_kv.readline()
        if l1:
            l2=cutesv_kv.readline()
            if l1 in fnb_set:
                splits = re.split('\s+', l2)
                sv_start = int(splits[1])
                sv_len = int(splits[4])
                sv_type = splits[3]
                sv_in_cutesv.append([sv_start,sv_len,sv_type,0])
        else:
            break
    cutesv_kv.close()
    while True:
        l=CNNSSV_candidate.readline()
        if l:
            splits=re.split('\s+',l)
            sv_start=int(splits[1])
            sv_len=int(splits[4])
            sv_type=splits[3]
            find_flag=False
            for r in sv_in_cutesv:
                if abs(sv_start-r[0])<=20 and sv_type==r[2] and abs(sv_len-r[1])<=20:
                    find_flag=True
                    fout.write(l)
                    r[3]=1
                    break
        else:
            break
    # for l in sv_in_cutesv:
    #     if l[3]==0:
    #         print(l)
    fout.close()







