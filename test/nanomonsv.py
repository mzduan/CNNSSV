import re
if __name__ == '__main__':


    bk_list=list()
    forward_bk1=0
    forward_bk2=0

    with open('/Users/duan/Desktop/results/tumor.nanomonsv.result.txt','r') as fin:
        while True:
            l=fin.readline()
            if l:
                infos=re.split('\s+',l)
                if infos[0]=="chr20":
                    bk1=int(infos[1])
                    bk2=int(infos[4])
                    if abs(bk1-forward_bk1)<=20 and abs(bk2-forward_bk2) <=20:
                        forward_bk1=bk1
                        forward_bk2=bk2
                    else:
                        bk_list.append([bk1,bk2])
                        forward_bk1=bk1
                        forward_bk2=bk2
            else:
                break
    print(len(bk_list))



