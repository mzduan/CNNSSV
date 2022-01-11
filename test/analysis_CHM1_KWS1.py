import re
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
if __name__ == '__main__':

    #画一下deletion长度的分布
    del_fin=open('/Users/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_sim_tumor_del.bed','r')
    ins_fin=open('/Users/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_sim_tumor_ins.bed','r')
    # inv_fin=open('/Users/duan/Downloads/文档/论文/somatic_SV/cuteSV/cuteSV-master/simulation/sim_inv.bed','r')
    dup_fin=open('/Users/duan/Desktop/getBreakpoint/groundtruth/random_sv/chr20_sim_tumor_dup.bed','r')
    # len_dict=dict()
    del_len_list=list()
    while True:
        l=del_fin.readline()
        if l:
            splits=re.split('\s+',l)
            del_start=splits[1]
            del_end=splits[2]
            sv_len=int(del_end)-int(del_start)
            del_len_list.append(sv_len/1000)
        else:
            break
    del_fin.close()


    ins_len_list=list()
    while True:
        l=ins_fin.readline()
        if l:
            splits=re.split('\s+',l)
            insert_seq=splits[4]
            sv_len=len(insert_seq)
            ins_len_list.append(sv_len/1000)
        else:
            break
    ins_fin.close()


    dup_len_list=list()
    while True:
        l=dup_fin.readline()
        if l:
            splits=re.split('\s+',l)
            dup_start=splits[1]
            dup_end=splits[2]
            sv_len=int(dup_end)-int(dup_start)
            # dup_len_list.append(sv_len/1000)
            # if sv_len<30000:
            dup_len_list.append(sv_len / 1000)
        else:
            break
    dup_fin.close()


    # inv_len_list=list()
    # while True:
    #     l=inv_fin.readline()
    #     if l:
    #         splits=re.split('\s+',l)
    #         inv_start=splits[1]
    #         inv_end=splits[2]
    #         sv_len=int(inv_end)-int(inv_start)
    #         inv_len_list.append(sv_len/1000)
    #     else:
    #         break
    # inv_fin.close()

    print(max(del_len_list))
    del_ecdf = sm.distributions.ECDF(del_len_list)
    x = np.linspace(0, max(del_len_list))
    y = del_ecdf(x)
    plt.plot(x, y, linewidth = '1',label='DEL',color='r')


    print(max(ins_len_list))
    ins_ecdf = sm.distributions.ECDF(ins_len_list)
    x = np.linspace(0, max(ins_len_list))
    y = ins_ecdf(x)
    plt.plot(x, y, linewidth = '1',label='INS',color='g')
    # #
    print(max(dup_len_list))
    dup_ecdf = sm.distributions.ECDF(dup_len_list)
    x = np.linspace(0, max(dup_len_list))
    y = dup_ecdf(x)
    plt.plot(x, y, linewidth = '1',label='DUP',color='b')
    # #
    # print(max(inv_len_list))
    # inv_ecdf = sm.distributions.ECDF(inv_len_list)
    # x = np.linspace(0, max(inv_len_list))
    # y = inv_ecdf(x)
    # plt.plot(x, y, linewidth = '1',label='INV',color='c')


    # plt.xticks(np.arange(0, 25, 5))
    # plt.yticks(np.arange(0, 1.01, 0.2))
    #
    plt.xlabel("SV Length(kb)", fontsize=10)
    plt.ylabel("CDF", fontsize=10)
    plt.legend(loc='lower right')
    plt.savefig('/Users/duan/Desktop/INV变异长度分布.png')

