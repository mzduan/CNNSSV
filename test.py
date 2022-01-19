import CNN
import torch
import TestSet
from torch.utils.data import DataLoader
import re
import torch.nn as nn
import matplotlib.pyplot as plt
import sys
import numpy as np
from sklearn.metrics import roc_curve, auc

def is_somatic(gd,chrom,start,end,sv_type):
    for g in gd:
        if g[3] == chrom and g[2] == sv_type:
            if abs(int(g[0]) - start) <= 200 and abs(int(g[1]) - end) <= 200:
                return True

    return False
def get_gd():
    groundtruth=list()
    with open('/home/mzduan/somaticSV/sv/chr20.somatic.bed','r') as fin:
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
    return groundtruth
# if __name__ == '__main__':
#
#     # model_path=sys.argv[1]
#     # features_path=sys.argv[2]
#     # out_path=sys.argv[3]
#
#     model_path='/Users/duan/Desktop/results/somaticSV/cnn.edition2.model'
#     features_path='/Users/duan/Desktop/results/somaticSV/tag/bam_0.7/chr20/germline'
#
#
#     cnn = CNN.CNN()
#     cnn.load_state_dict(torch.load(model_path))
#
#
#     test_set=TestSet.TestSet(features_path)
#     test_loader=DataLoader(test_set,batch_size=1,shuffle=True)
#
#
#     correct_count=0
#     error_count=0
#
#     for step, (batch_x, batch_sup_x,file_name) in enumerate(test_loader):
#
#         output = cnn.forward(batch_x,batch_sup_x)
#         if torch.argmax(output)==0:
#             correct_count=correct_count+1
#         else:
#             print(file_name)
#             error_count=error_count+1
    #    # print(correct_count,error_count)

def predict(model_path,features_path,out_path,purity):

    cnn = CNN.CNN()
    cnn.load_state_dict(torch.load(model_path))
    test_set=TestSet.TestSet(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)

    # fout=open(out_path,'w')

    groundtruth=get_gd()


    test_list=list()
    predicts=list()

    for step, (x,sup_x,file_name) in enumerate(test_loader):

        file_name=file_name[0]
        output = cnn.forward(x,sup_x)
        # print(output)
        splits = re.split('_', file_name)
        support_counts = int(splits[4])
        chro = splits[0]
        sv_type = splits[1]
        start = int(splits[2])
        end = start + int(splits[3])

        if is_somatic(groundtruth,chro,start,end,sv_type):
            print(1)
            test_list.append(1)
        else:
            print(0)
            test_list.append(0)

        #进行softmax
        soft_max=nn.Softmax(dim=1)
        soft_output=soft_max(output)
        numpy_output=soft_output.detach().numpy()
        # print(numpy_output)
        print(numpy_output[0][1])
        predicts.append(numpy_output[0][1])

        # if torch.argmax(output)==1:
        #     if sv_type=='INS':
        #         end=start+1
        #     fout.write(chro+'\t'+str(start)+'\t'+str(end)+'\t'+sv_type+'\t'+str(splits[3])+'\n')
        # else:
        #     if support_counts>=3:
        #         if sv_type == 'INS':
        #             end = start + 1
        #         fout.write(chro + '\t' + str(start) + '\t' + str(end) + '\t' + sv_type + '\t' + str(splits[3]) + '\n')
        # print("not a somatic sv")
    # fout.close()
    fpr_lr, tpr_lr, thres_lr = roc_curve(test_list,predicts)

    roc_auc=auc(fpr_lr,tpr_lr)
    print("AUC为：\t",roc_auc)

    np.save('home/mzduan/somaticSV/roc_data/fpr_'+str(purity)+'.dat',fpr_lr)
    np.save('home/mzduan/somaticSV/roc_data/tpr_'+str(purity)+'.dat', tpr_lr)
    # plt.figure()
    # plt.plot(fpr_lr,tpr_lr,color='darkorange',lw=2,label='ROC cureve(area=%0.2f)' % roc_auc)
    # plt.plot([0,1],[0,1],color='navy',lw=2,linestyle='--')
    # plt.xlim([0.0,1.0])
    # plt.ylim([0.0,1.05])
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.title('ROC cureve')
    # plt.legend(loc='lower right')
    # plt.savefig('/home/mzduan/somaticSV/simulate_chr20_0.5.png')
    # plt.close()

