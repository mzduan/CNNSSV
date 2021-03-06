import re
if __name__ == '__main__':

    tags = ['500','1000','1500','2000','2500']
    # tags = ['2', '3', '4', '5', '6', '7','8']
    for t in tags:

        predict_bed='/home/duan/Desktop/getBreakpoint/results/vary_sv_len/sniffles/sniffles_somatic_'+t+'.bed'
        # predict_bed='/Users/duan/Desktop/getBreakpoint/results/simulate/nanomonsv/20_0.3.tumor.nanomonsv.result.bed'
        # predict_bed='/Users/duan/Downloads/chr20_0.2_predict.bed'
        # fn_name='/home/duan/Desktop/getBreakpoint/results/simulate/CNN/11_9/chr20_0.7_simulate_somatic.fn.bed'
        # fn_name='/Users/duan/Desktop/fn/sniffles/sniffles_simulate_chr20_0.'+t+'.fn.txt'

        predict=list()
        with open(predict_bed,'r') as fin:
            while True:
                l=fin.readline()
                if l:
                    splits=re.split('\s+',l)
                    chrom=splits[0]
                    start=splits[1]
                    end=splits[2]
                    sv_type=splits[3]
                    predict.append((start,end,sv_type,chrom))
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
        with open('/home/duan/Desktop/getBreakpoint/results/vary_sv_len/gd/chr20.'+t+'.somatic.bed','r') as fin:
            while True:
                l=fin.readline()
                if l:
                    splits=re.split('\s+',l)
                    chrom=splits[0]
                    start=splits[1]
                    end=splits[2]
                    sv_type=splits[3]
                    if sv_type=='insertion' or sv_type=='INS':
                        groundtruth.append((start,end,'INS',chrom))
                    elif sv_type=='deletion' or sv_type=='DEL':
                        groundtruth.append((start, end, 'DEL',chrom))
                    elif sv_type=='inversion' or sv_type=='INV':
                        groundtruth.append((start, end, 'INV',chrom))
                    elif sv_type=='tandem' or sv_type=='DUP':
                        groundtruth.append((start,end,'DUP',chrom))
                else:
                    break
        true_p=set()
        true_g=set()
        for p in predict:
            for g in groundtruth:
                if p[3]==g[3] and p[2]==g[2]:
                    if abs(int(p[0])-int(g[0]))<=200 and abs(int(p[1])-int(g[1]))<=200:
                        true_p.add(p)
                    #     break
        for g in groundtruth:
            find_flag = False
            for p in predict:
                if p[3] == g[3] and g[2]==p[2]:
                    if abs(int(g[0])-int(p[0]))<=200 and abs(int(g[1])-int(p[1]))<=200:
                        true_g.add(g)
                        find_flag=True
                        break

        # print("FN:")
        # fn=0
        # with open(fn_name,'w') as fout:
        #     for q in groundtruth:
        #         if q not in true_g:
        #             # print(q)
        #             fout.write(str(q[0])+'\t'+str(q[1])+'\t'+str(q[2])+'\t'+str(q[3])+'\n')
        #             fn=fn+1
        #     print(fn)

        # print("FP:")
        # fp=0
        # with open(fp_name, 'w') as fout:
        #     for p in predict:
        #         if p not in true_p:
        #             fout.write(str(p[0]) + '\t' + str(p[1]) + '\t' + str(p[2]) + '\t'+str(p[3])+'\n')
        #             # fout.write('chr20' + '\t' + str(p[0]) + '\t' + str(p[1]) + '\t' + str(p[2]) + '\n')
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
        # print("support read:",t)
        print("\tmean_sv_len:",t)
        print("\t\tRecall:\t",recall)
        print("\t\tPrecision:\t",precision)
        print("\t\tF1:\t",2*recall*precision/(recall+precision))





