import re
if __name__ == '__main__':
    fin=open('/home/duan/Desktop/getBreakpoint/results/simulate/CNN/11_14_with_no_sup/chr20_0.7_simulate_somatic.bed','r')
    fout=open('/home/duan/Desktop/getBreakpoint/results/simulate/CNN/11_14_with_no_sup/chr20_0.7_simulate_somatic.bigger50.bed','w')
    while True:
        l=fin.readline()
        if l:
            splits=re.split('\s+',l)
            sv_len=int(splits[4])
            if sv_len>=50:
                fout.write(l)
        else:
            break

    fin.close()
    fout.close()

