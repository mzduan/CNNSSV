import Siamese
import torch
import SiameseTestDataset
from torch.utils.data import DataLoader
import re
def predict(model_path,features_path,out_path):
    siamese = Siamese.Siamese()
    siamese.load_state_dict(torch.load(model_path))
    test_set=SiameseTestDataset.SiameseTestNetworkDataset(features_path)
    test_loader=DataLoader(test_set,batch_size=1,shuffle=True)

    fout=open(out_path,'w')

    for step, (batch_n,batch_t,file_name) in enumerate(test_loader):
        file_name=file_name[0]
        output = siamese(batch_n,batch_t)
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
            print(file_name+"not a somatic sv")
    fout.close()