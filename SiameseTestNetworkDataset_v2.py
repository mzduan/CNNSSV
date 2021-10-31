import torch.utils.data as data
import numpy as np
import os
import torch
from PIL import Image


class SiameseTestNetworkDataset(data.Dataset):
    def __init__(self, feat_path):
        self.normal_features = list()
        self.tumor_features = list()
        self.sup_features = list()
        self.file_names = list()
        for f in os.listdir(feat_path):
            splits = f.split('_')
            if len(splits) == 4:
                absolute_path = feat_path + '/' + f
                for image in os.listdir(absolute_path):
                    if image[0] == 'n':
                        n_feature = np.zeros((3, 50, 500))
                        normal = Image.open(absolute_path + '/' + image)
                        normal = np.array(normal)
                        n_feature[0] = normal[:, :, 0]
                        n_feature[1] = normal[:, :, 1]
                        n_feature[2] = normal[:, :, 2]
                        self.normal_features.append(n_feature)
                    elif image[0] == 't':
                        t_feature = np.zeros((3, 50, 500))
                        tumor = Image.open(absolute_path + '/' + image)
                        tumor = np.array(tumor)
                        t_feature[0] = tumor[:, :, 0]
                        t_feature[1] = tumor[:, :, 1]
                        t_feature[2] = tumor[:, :, 2]
                        self.tumor_features.append(t_feature)
                    elif image[0] == 's':
                        sup_feat = np.load(absolute_path + '/' + image)
                        self.sup_features.append(sup_feat)
                self.file_names.append(f)

    def __len__(self):
        return len(self.normal_features)

    def __getitem__(self, index):
        return torch.tensor(self.normal_features[index], dtype=torch.float),torch.tensor(self.tumor_features[index], dtype=torch.float),\
               torch.tensor(self.sup_features[index],dtype=torch.float), self.file_names[index]
