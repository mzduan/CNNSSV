import CNN
import torch
import TestSet
from torch.utils.data import DataLoader
if __name__ == '__main__':
    cnn = CNN.CNN()
    model=torch.load('/home/duan/Desktop/somaticSV/cnn_10_21.model')
    for k in model.keys():
        print(k,model[k].shape)