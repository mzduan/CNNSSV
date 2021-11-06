import torch.utils.data as data
import numpy as np
import os
import torch
from PIL import Image
class SiameseTrainNetworkDataset(data.Dataset):
    def __init__(self,ccs_feat_path):
        self.sup_features=list()
        self.normal_features=list()
        self.tumor_features = list()
        self.labels = list()
        for p in ["bam_0.2", "bam_0.5", "bam_0.7"]:
            for c in range(1, 23, 1):
                if c==20:
                    continue
                current_feat_path = ccs_feat_path + '/' + p + '/chr' + str(c)
                germline_path=current_feat_path+'/germline'
                for f in os.listdir(germline_path):
                    if f[0] != '.':
                        absolute_path = germline_path + '/' + f
                        n_flag=False
                        t_flag=False
                        s_flag=False

                        n_feature = np.zeros((3, 50, 500))
                        t_feature = np.zeros((3, 50, 500))
                        sup_feat = None
                        for image in os.listdir(absolute_path):
                            if image[0]=='n':
                                normal=Image.open(absolute_path+'/'+image)
                                normal=np.array(normal)
                                n_feature[0]=normal[:,:,0]
                                n_feature[1]=normal[:,:,1]
                                n_flag=True
                            elif image[0]=='t':
                                tumor=Image.open(absolute_path+'/'+image)
                                tumor=np.array(tumor)
                                t_feature[0]=tumor[:,:,0]
                                t_feature[1]=tumor[:,:,1]
                                t_feature[2]=tumor[:,:,2]
                                t_flag=True
                            elif image[0]=='s':
                                sup_feat=np.load(absolute_path+'/'+image)
                                s_flag=True
                        if n_flag==True and t_flag==True and s_flag==True:
                            self.normal_features.append(n_feature)
                            self.tumor_features.append(t_feature)
                            self.sup_features.append(sup_feat)
                            self.labels.append(0)
                somatic_path=current_feat_path+'/somatic'
                for f in os.listdir(somatic_path):
                    if f[0] != '.':
                        absolute_path = somatic_path + '/' + f
                        n_flag=False
                        t_flag=False
                        s_flag=False

                        n_feature = np.zeros((3, 50, 500))
                        t_feature = np.zeros((3, 50, 500))
                        sup_feat = None
                        for image in os.listdir(absolute_path):
                            if image[0]=='n':
                                normal=Image.open(absolute_path+'/'+image)
                                normal=np.array(normal)
                                n_feature[0]=normal[:,:,0]
                                n_feature[1]=normal[:,:,1]
                                n_feature[2]=normal[:,:,2]
                                n_flag = True
                            elif image[0]=='t':
                                tumor=Image.open(absolute_path+'/'+image)
                                tumor=np.array(tumor)
                                t_feature[0]=tumor[:,:,0]
                                t_feature[1]=tumor[:,:,1]
                                t_feature[2]=tumor[:,:,2]
                                t_flag = True
                            elif image[0]=='s':
                                sup_feat=np.load(absolute_path+'/'+image)
                                s_flag = True
                        if n_flag==True and t_flag==True and s_flag==True:
                            self.normal_features.append(n_feature)
                            self.tumor_features.append(t_feature)
                            self.sup_features.append(sup_feat)
                            self.labels.append(1)


    def __len__(self):
        return len(self.labels)



    def __getitem__(self, index):
        return torch.tensor(self.normal_features[index],dtype=torch.float),torch.tensor(self.tumor_features[index],dtype=torch.float),torch.tensor(self.sup_features[index],dtype=torch.float),torch.tensor(self.labels[index],dtype=torch.long)