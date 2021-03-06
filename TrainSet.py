import torch.utils.data as data
import numpy as np
import os
import torch
from PIL import Image
class TrainSet(data.Dataset):
    def __init__(self,ccs_feat_path):
        self.sup_features=list()
        self.features=list()
        self.labels = list()
        for p in ["bam_0.2", "bam_0.5", "bam_0.7"]:
        # for p in ["bam_0.7"]:
            for c in range(1, 23, 1):

                if c==20:
                    continue
                current_feat_path = ccs_feat_path + '/' + p + '/chr' + str(c)
                print("load features "+current_feat_path+" germline")
                germline_path=current_feat_path+'/germline'
                for f in os.listdir(germline_path):
                    if f[0] != '.':
                        absolute_path = germline_path + '/' + f
                        sub_feature=np.zeros((6, 50, 500))

                        n_flag=False
                        t_flag=False
                        sup_flag=False

                        for image in os.listdir(absolute_path):
                            if image[0]=='n':
                                try:
                                    normal=Image.open(absolute_path+'/'+image)
                                    normal = np.array(normal)
                                    # normal = np.load(absolute_path + '/' + image)
                                    sub_feature[3] = normal[:, :, 0]
                                    sub_feature[4] = normal[:, :, 1]
                                    sub_feature[5] = normal[:, :, 2]
                                    n_flag=True
                                except:
                                    print("Error in load "+absolute_path+'/'+image)
                            elif image[0]=='t':
                                # print(absolute_path + '/' + image)
                                try:
                                    tumor=Image.open(absolute_path+'/'+image)
                                    tumor = np.array(tumor)
                                    # tumor = np.load(absolute_path + '/' + image)
                                    sub_feature[0] = tumor[:, :, 0]
                                    sub_feature[1] = tumor[:, :, 1]
                                    sub_feature[2] = tumor[:, :, 2]
                                    t_flag = True
                                except:
                                    print("Error in load " + absolute_path + '/' + image)
                            elif image[0]=='s':
                                # print(absolute_path + '/' + image)
                                try:
                                    sup_feat=np.load(absolute_path+'/'+image)
                                    self.sup_features.append(sup_feat)
                                    sup_flag = True
                                except:
                                    print("Error in load " + absolute_path + '/' + image)

                        if n_flag and t_flag and sup_flag:
                            self.features.append(sub_feature)
                            self.labels.append(0)
                somatic_path=current_feat_path+'/somatic'
                print("load features " + current_feat_path + " somatic")
                for f in os.listdir(somatic_path):
                    if f[0] != '.':
                        absolute_path = somatic_path + '/' + f
                        sub_feature=np.zeros((6, 50, 500))

                        n_flag=False
                        t_flag=False
                        sup_flag=False
                        for image in os.listdir(absolute_path):
                            if image[0]=='n':
                                # print(absolute_path + '/' + image)
                                try:
                                    normal=Image.open(absolute_path+'/'+image)
                                    normal = np.array(normal)
                                    # normal = np.load(absolute_path + '/' + image)
                                    sub_feature[3] = normal[:, :, 0]
                                    sub_feature[4] = normal[:, :, 1]
                                    sub_feature[5] = normal[:, :, 2]
                                    n_flag=True
                                except:
                                    print("Error in load " + absolute_path + '/' + image)
                            elif image[0]=='t':
                                # print(absolute_path + '/' + image)
                                try:
                                    tumor=Image.open(absolute_path+'/'+image)
                                    tumor = np.array(tumor)
                                    # tumor = np.load(absolute_path + '/' + image)
                                    sub_feature[0] = tumor[:, :, 0]
                                    sub_feature[1] = tumor[:, :, 1]
                                    sub_feature[2] = tumor[:, :, 2]
                                    t_flag=True
                                except:
                                    print("Error in load " + absolute_path + '/' + image)
                            elif image[0] == 's':
                                # print(absolute_path + '/' + image)
                                try:
                                    sup_feat = np.load(absolute_path+'/'+image)
                                    self.sup_features.append(sup_feat)
                                    sup_flag=True
                                except:
                                    print("Error in load " + absolute_path + '/' + image)

                        if n_flag and t_flag and sup_flag:
                            self.features.append(sub_feature)
                            self.labels.append(1)
    def __len__(self):
        return len(self.labels)



    def __getitem__(self, index):
        return torch.tensor(self.features[index],dtype=torch.float),torch.tensor(self.sup_features[index], dtype=torch.float),\
               torch.tensor(self.labels[index],dtype=torch.long)
