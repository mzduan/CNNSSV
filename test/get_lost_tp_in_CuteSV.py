if __name__ == '__main__':
    tumor_tp=open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.tumor7.tp','r')
    somatic_tp=open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.somatic7.tp','r')

    somatic_lost_tp = open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.somatic7.lost_tp.txt', 'w')

    tumor_lines=set()
    somatic_lines=set()

    while True:
        l=tumor_tp.readline()
        if l:
            tumor_lines.add(l)
        else:
            break
    while True:
        l=somatic_tp.readline()
        if l:
            somatic_lines.add(l)
        else:
            break

    for l in tumor_lines:
        if l not in somatic_lines:
            somatic_lost_tp.write(l)

    tumor_tp.close()
    somatic_tp.close()
    somatic_lost_tp.close()




