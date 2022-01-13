import re

if __name__ == '__main__':
    del_counts=0
    ins_counts=0
    inv_counts=0
    dup_counts=0


    fin=open('/Users/duan/Desktop/sniffles.fp.txt','r')
    while True:
        l=fin.readline()
        if l:
            infos=re.split('\s+',l)
            sv_type=infos[2]

            if sv_type=='INS':
                ins_counts+=1
            elif sv_type=='INV':
                inv_counts+=1
            elif sv_type=='DUP':
                dup_counts+=1
            elif sv_type=='DEL':
                del_counts+=1
        else:
            break
    print(del_counts)
    print(ins_counts)
    print(inv_counts)
    print(dup_counts)