import re
if __name__ == '__main__':

    predict_bed='/home/duan/Desktop/getBreakpoint/results/random/nanomonsv/0.7.tumor.nanomonsv.result.bed'
    # predict_bed='/Users/duan/Desktop/results/somaticSV/callset/mix/0.2/sniffles.somatic.bed'
    # predict_bed='/Users/duan/Downloads/chr20_0.2_predict.bed'
    # fn_name='/Users/duan/Desktop/results/somaticSV/callset/CCS/0.2/chr20/nanomonsv.fn.txt'
    # fp_name='/home/duan/Desktop/getBreakpoint/results/simulate/CNN/11_14_with_no_sup/chr20_0.7_simulate_somatic.fp'

    predict=list()
    with open(predict_bed,'r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                start=splits[1]
                end=splits[2]
                sv_type=splits[3]
                predict.append((start,end,sv_type))
            else:
                break

    # predict=list()
    # forward_bk1=0
    # forward_bk2=0
    #
    # with open('/Users/duan/Desktop/results/somaticSV/NA19238_NA19239/0.7.tumor.nanomonsv.result.txt','r') as fin:
    #     while True:
    #         l=fin.readline()
    #         if l:
    #             infos=re.split('\s+',l)
    #             if infos[0]=="chr20":
    #                 bk1=int(infos[1])
    #                 bk2=int(infos[4])
    #                 if abs(bk1-forward_bk1)<=20 and abs(bk2-forward_bk2) <=20:
    #                     forward_bk1=bk1
    #                     forward_bk2=bk2
    #                 else:
    #                     predict.append((bk1,bk2))
    #                     forward_bk1=bk1
    #                     forward_bk2=bk2
    #         else:
    #             break




    groundtruth=list()
    with open('/home/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_somatic.bed','r') as fin:
        while True:
            l=fin.readline()
            if l:
                splits=re.split('\s+',l)
                start=splits[1]
                end=splits[2]
                sv_type=splits[3]
                if sv_type=='insertion' or sv_type=='INS':
                    groundtruth.append((start,end,'INS'))
                elif sv_type=='deletion' or sv_type=='DEL':
                    groundtruth.append((start, end, 'DEL',0))
                elif sv_type=='inversion' or sv_type=='INV':
                    groundtruth.append((start, end, 'INV',0))
                elif sv_type=='tandem' or sv_type=='DUP':
                    groundtruth.append((start,end,'DUP'))
            else:
                break
    true_p=set()
    true_g=set()
    for p in predict:
        for g in groundtruth:
            if p[2]==g[2]:
                if abs(int(p[0])-int(g[0]))<=50 and abs(int(p[1])-int(g[1]))<=50:
                    true_p.add(p)
                #     break
    for g in groundtruth:
        find_flag = False
        for p in predict:
            if g[2]==p[2]:
                if abs(int(g[0])-int(p[0]))<=50 and abs(int(g[1])-int(p[1]))<=50:
                    true_g.add(g)
                    find_flag=True
                    break
        # if find_flag==False:
        #     print(g)

    # print("FN:")
    # fn=0
    # with open(fn_name,'w') as fout:
    #     for q in groundtruth:
    #         if q not in true_g:
    #             # print(q)
    #             fout.write('chr20'+'\t'+str(q[0])+'\t'+str(q[1])+'\t'+str(q[2])+'\n')
                # fn=fn+1
        # print(fn)

    # print("FP:")
    # fp=0
    # with open(fp_name, 'w') as fout:
    #     for p in predict:
    #         if p not in true_p:
    #             # print(p)
    #             fout.write('chr20' + '\t' + str(p[0]) + '\t' + str(p[1]) + '\t' + str(p[2]) + '\n')
    #             fp=fp+1
    # print(fp)


    # for q in groundtruth:
    #     if q[3]==1:
    #         true_g=true_g+1
    # for q in predict:
    #     if q[3]==1:
    #         true_p=true_p+1
    #     if q not in true_g:
    #         print(q)
    #         fn=fn+1
    # print(fn)

    # print(len(true_p))
    # print(len(true_g))

    # print(len(true_p),len(predict),len(groundtruth))

    recall=len(true_g)/len(groundtruth)
    precision=len(true_p)/len(predict)

    print("Recall:\t",recall)
    print("Precision:\t",precision)
    print("F1:\t",2*recall*precision/(recall+precision))





