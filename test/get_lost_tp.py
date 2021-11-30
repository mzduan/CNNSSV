if __name__ == '__main__':
    f1=open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.tumor7.tp','r')
    f2=open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.somatic7.tp','r')


    f3=open('/home/duan/Desktop/getBreakpoint/results/mixed/Siamese/11_12/0.2.Siamese&cutesv.fnb','w')

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
