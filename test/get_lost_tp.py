if __name__ == '__main__':
    f1=open('/home/duan/Desktop/somaticSV/callset/NA19239_NA19240_mixed/0.7.cutesv.tb','r')
    f2=open('/home/duan/Desktop/somaticSV/callset/NA19239_NA19240_mixed/CNNSSV_MIXED/v1/0.7.CNNSSV.tb','r')


    f3=open('/home/duan/Desktop/somaticSV/callset/NA19239_NA19240_mixed/CNNSSV_MIXED/v1/0.7.CNNSSV&cutesv.fnb','w')

    candidate_lines=set()
    somatic_lines=set()

    while True:
        l=f1.readline()
        if l:
            # if l in candidate_lines:
            #     print(l)
            candidate_lines.add(l)
        else:
            break

    while True:
        l=f2.readline()
        if l:
            somatic_lines.add(l)
        else:
            break

    print(len(somatic_lines))
    print(len(candidate_lines))
    for c in candidate_lines:
        if c not in somatic_lines:
            f3.write(c)
    f1.close()
    f2.close()
    f3.close()
