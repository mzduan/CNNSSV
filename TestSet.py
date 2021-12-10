import torch.utils.data as data
import numpy as np
import os
import torch
from PIL import Image
class TestSet(data.Dataset):
    def __init__(self,feat_path):
        self.features=list()
        self.sup_features=list()
        self.file_names=list()

        n_flag = False
        t_flag = False
        sup_flag = False



        for f in os.listdir(feat_path):
            splits=f.split('_')
            if len(splits)==5:
                absolute_path=feat_path+'/'+f
                sub_feature = np.zeros((6, 50, 500))
                for image in os.listdir(absolute_path):
                    if image[0] == 'n':
                        try:
                            normal = Image.open(absolute_path + '/' + image)
                            normal = np.array(normal)
                            sub_feature[3] = normal[:, :, 0]
                            sub_feature[4] = normal[:, :, 1]
                            sub_feature[5] = normal[:, :, 2]
                            n_flag = True
                        except:
                            print("Error in load " + absolute_path + '/' + image)
                    elif image[0] == 't':
                        try:
                            tumor = Image.open(absolute_path + '/' + image)
                            tumor = np.array(tumor)
                            sub_feature[0] = tumor[:, :, 0]
                            sub_feature[1] = tumor[:, :, 1]
                            sub_feature[2] = tumor[:, :, 2]
                            t_flag=True
                        except:
                            print("Error in load " + absolute_path + '/' + image)
                    elif image[0] == 's':
                        try:
                            sup_feat = np.load(absolute_path + '/' + image)
                            self.sup_features.append(sup_feat)
                            sup_flag=True
                        except:
                            print("Error in load " + absolute_path + '/' + image)

                if n_flag and t_flag and sup_flag:
                    self.features.append(sub_feature)
                    self.file_names.append(f)

    def __len__(self):
        return len(self.features)



    def __getitem__(self, index):
        return torch.tensor(self.features[index],dtype=torch.float),torch.tensor(self.sup_features[index], dtype=torch.float),\
               self.file_names[index]
