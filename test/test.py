import re
if __name__ == '__main__':
    f1=open('/home/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_germline.bed','r')
    f2=open('/home/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_tumor.bed','r')

    f3=open('/home/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_somatic.bed','w')
    normal_sv=set()
    tumor_sv=set()
    while True:
        l=f1.readline()
        if l:
            normal_sv.add(l)
        else:
            break

    while True:
        l=f2.readline()
        if l:
            tumor_sv.add(l)
        else:
            break

    somatic_counts=0
    for i in tumor_sv:
        if i not in normal_sv:
            somatic_counts+=1
            f3.write(i)

    print(len(normal_sv))
    print(len(tumor_sv))
    print(somatic_counts)


    f1.close()
    f2.close()
    f3.close()

