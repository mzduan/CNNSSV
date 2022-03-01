import re
if __name__ == '__main__':

    cutesv_callset=set()
    sniffles_callset=set()
    nanomonsv_callset=set()
    CNNSSV_callset=set()

    distinct_callset=set()


    with open('/Users/duan/Desktop/1_sv.bed','r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                chro=splits[0]
                sv_start=int(splits[1])
                sv_end=int(splits[2])
                sv_type = splits[3]
                sv_len = int(splits[4])
                cutesv_callset.add((chro,sv_start,sv_end,sv_type,sv_len))
                distinct_callset.add((chro,sv_start,sv_end,sv_type,sv_len))
            else:
                break

    with open('/Users/duan/Desktop/2_sv.bed','r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                chro=splits[0]
                sv_start=int(splits[1])
                sv_end=int(splits[2])
                sv_type = splits[3]
                sv_len = int(splits[4])
                sniffles_callset.add((chro,sv_start,sv_end,sv_type,sv_len))
            else:
                break

    with open('/Users/duan/Desktop/5_sv.bed','r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                chro=splits[0]
                sv_start=int(splits[1])
                sv_end=int(splits[2])
                sv_type = splits[3]
                sv_len = int(splits[4])
                CNNSSV_callset.add((chro,sv_start,sv_end,sv_type,sv_len))
            else:
                break

    with open('/Users/duan/Desktop/6_sv.bed','r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                chro=splits[0]
                sv_start=int(splits[1])
                sv_end=int(splits[2])
                sv_type = splits[3]
                sv_len = int(splits[4])
                nanomonsv_callset.add((chro,sv_start,sv_end,sv_type,sv_len))
            else:
                break


    for i in sniffles_callset:
        find_flag = False
        for j in distinct_callset:
            if i[0]==j[0] and i[3]==j[3]:
                if abs(i[1]-j[1])<=50 and abs(i[4]-j[4])<=50:
                    find_flag=True
        if not find_flag:
            distinct_callset.add(i)

    for i in CNNSSV_callset:
        find_flag = False
        for j in distinct_callset:
            if i[0]==j[0] and i[3]==j[3]:
                if abs(i[1]-j[1])<=50 and abs(i[4]-j[4])<=50:
                    find_flag=True
        if not find_flag:
            distinct_callset.add(i)

    for i in nanomonsv_callset:
        find_flag = False
        for j in distinct_callset:
            if i[0]==j[0] and i[3]==j[3]:
                if abs(i[1]-j[1])<=50 and abs(i[4]-j[4])<=50:
                    find_flag=True
        if not find_flag:
            distinct_callset.add(i)


    # print(len(cutesv_callset))
    # print(len(sniffles_callset))
    # print(len(CNNSSV_callset))
    # print(len(nanomonsv_callset))
    # print(len(distinct_callset))


    sum=0
    for i in distinct_callset:
        cutesv_find_flag=False
        sniffles_find_flag=False
        CNNSSV_find_flag=False
        nanomonsv_find_flag=False
        for j in cutesv_callset:
            if i[0] == j[0] and i[3] == j[3]:
                if abs(i[1] - j[1]) <= 50 and abs(i[4] - j[4]) <= 50:
                    cutesv_find_flag = True
        for j in sniffles_callset:
            if i[0] == j[0] and i[3] == j[3]:
                if abs(i[1] - j[1]) <= 50 and abs(i[4] - j[4]) <= 50:
                    sniffles_find_flag = True
        for j in CNNSSV_callset:
            if i[0] == j[0] and i[3] == j[3]:
                if abs(i[1] - j[1]) <= 50 and abs(i[4] - j[4]) <= 50:
                    CNNSSV_find_flag = True
                    # print(i,j)
        for j in nanomonsv_callset:
            if i[0] == j[0] and i[3] == j[3]:
                if abs(i[1] - j[1]) <= 50 and abs(i[4] - j[4]) <= 50:
                    nanomonsv_find_flag = True



        if not cutesv_find_flag and not sniffles_find_flag and not nanomonsv_find_flag and CNNSSV_find_flag:
            sum+=1
    print(sum)
