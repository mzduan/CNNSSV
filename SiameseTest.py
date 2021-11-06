import Siamese_v1
import torch
import SiameseTestNetworkDataset_v1
from torch.utils.data import DataLoader
import re
import sys
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
#     #
#     # print(correct_count,error_count)

def predict(model_path,features_path,out_path):
    siamese = Siamese_v1.Siamese_V1()
    siamese.load_state_dict(torch.load(model_path))
    test_set=SiameseTestNetworkDataset_v1.SiameseTestNetworkDataset(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)

    fout=open(out_path,'w')

    for step, (batch_n,batch_t,batch_nv,batch_tv,file_name) in enumerate(test_loader):
        file_name=file_name[0]
        output = siamese.forward(batch_n,batch_t,batch_nv,batch_tv)
        if torch.argmax(output)==1:
            splits=re.split('_',file_name)
            chro=splits[0]
            sv_type = splits[1]
            start=int(splits[2])
            end=start+int(splits[3])
            if sv_type=='INS':
                end=start+1
            fout.write(chro+'\t'+str(start)+'\t'+str(end)+'\t'+sv_type+'\t'+str(splits[3])+'\n')
        else:
            print("not a somatic sv")
    fout.close()