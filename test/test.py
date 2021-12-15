
if __name__ == '__main__':

    # recall=51.69
    # precision=26.51
    #
    # f1=2*recall*precision/(recall+precision)
    # print(f1)

    cutesv_somatic_fn=open('/home/duan/Desktop/cutesv.somatic7.fn','r')
    CNNSSV_somatic_fn = open('/home/duan/Desktop/CNNSSV.somatic7.fn', 'r')

    lost_tp=open('/home/duan/Desktop/CNNSSV.somatic7.lost.txt', 'w')
    cutesv_somatic_set=set()
    while True:
        l=cutesv_somatic_fn.readline()
        if l:
            cutesv_somatic_set.add(l)
        else:
            break

    while True:
        l=CNNSSV_somatic_fn.readline()
        if l:
            if l not in cutesv_somatic_set:
                lost_tp.write(l)
        else:
            break
    cutesv_somatic_fn.close()
    CNNSSV_somatic_fn.close()