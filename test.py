import CNN
import torch
import TestSet
from torch.utils.data import DataLoader
import re

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

def predict(model_path,features_path,out_path):

    cnn = CNN.CNN()
    cnn.load_state_dict(torch.load(model_path))
    test_set=TestSet.TestSet(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)

    fout=open(out_path,'w')

    # groundtruth=get_gd()

    for step, (x,sup_x,file_name) in enumerate(test_loader):

        file_name=file_name[0]
        output = cnn.forward(x,sup_x)

        splits = re.split('_', file_name)
        # support_counts = int(splits[4])
        chro = splits[0]
        sv_type = splits[1]
        start = int(splits[2])
        end = start + int(splits[3])

        if torch.argmax(output)==1:
            if sv_type=='INS':
                end=start+1
            fout.write(chro+'\t'+str(start)+'\t'+str(end)+'\t'+sv_type+'\t'+str(splits[3])+'\n')
    fout.close()


    # fpr_lr, tpr_lr, thres_lr = roc_curve(test_list,predicts)

    # roc_auc=auc(fpr_lr,tpr_lr)
    # print("AUC为：\t",roc_auc)

    # np.save('/home/mzduan/somaticSV/roc_data/heter_fpr_'+str(purity)+'.dat',fpr_lr)
    # np.save('/home/mzduan/somaticSV/roc_data/heter_tpr_'+str(purity)+'.dat', tpr_lr)

