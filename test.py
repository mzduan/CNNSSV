import CNN
import torch
import TestSet
from torch.utils.data import DataLoader
import re
import sys
if __name__ == '__main__':

    # model_path=sys.argv[1]
    # features_path=sys.argv[2]
    # out_path=sys.argv[3]

    model_path='/Users/duan/Desktop/results/somaticSV/cnn.edition2.model'
    features_path='/Users/duan/Desktop/results/somaticSV/tag/bam_0.7/chr20/germline'


    cnn = CNN.CNN()
    cnn.load_state_dict(torch.load(model_path))


    test_set=TestSet.TestSet(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)


    correct_count=0
    error_count=0

    for step, (batch_x, batch_sup_x,file_name) in enumerate(test_loader):

        output = cnn.forward(batch_x,batch_sup_x)
        if torch.argmax(output)==0:
            correct_count=correct_count+1
        else:
            print(file_name)
            error_count=error_count+1
    #
    # print(correct_count,error_count)

def predict(model_path,features_path,out_path):

    cnn = CNN.CNN()
    cnn.load_state_dict(torch.load(model_path))
    test_set=TestSet.TestSet(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)

    fout=open(out_path,'w')

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
        if torch.argmax(output)==1:
            if sv_type=='INS':
                end=start+1
            fout.write(chro+'\t'+str(start)+'\t'+str(end)+'\t'+sv_type+'\t'+str(splits[3])+'\n')
        else:
            if support_counts>=2:
                if sv_type == 'INS':
                    end = start + 1
                fout.write(chro + '\t' + str(start) + '\t' + str(end) + '\t' + sv_type + '\t' + str(splits[3]) + '\n')
        print("not a somatic sv")
    fout.close()