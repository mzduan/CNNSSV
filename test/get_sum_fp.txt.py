import re
if __name__ == '__main__':

    DEL_count = 0
    INS_count = 0
    INV_count = 0
    DUP_count = 0
    sum_count=0
    tags = ['2', '3', '4', '5', '6', '7','8']
    for t in tags:
        fp_name = '/Users/duan/Desktop/fn/nanomonsv/nanomonsv_simulate_chr20_0.'+t+'.fn.txt'

        with open(fp_name,'r') as fin:
            while True:
                l=fin.readline()
                if l:
                    sum_count+=1
                    infos=re.split('\s+',l)
                    sv_type=infos[2]
                    if sv_type=='DEL':
                        DEL_count+=1
                    elif sv_type=='INS':
                        INS_count+=1
                    elif sv_type=='INV':
                        INV_count+=1
                    elif sv_type=='DUP':
                        DUP_count+=1
                else:
                    break
    print("DEL count:",DEL_count)
    print("INS count:", INS_count)
    print("INV count:", INV_count)
    print("DUP count:", DUP_count)
    print(sum_count)