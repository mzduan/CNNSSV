import torch.nn as nn
import torch

#sup_feature为提取的特征向量
class Siamese_V2(nn.Module):
    def __init__(self):
        super(Siamese_V2, self).__init__()
        self.conv1 = nn.Sequential(    # 3*50*500  ->   16*48*498
            nn.Conv2d(
                in_channels=3,
                out_channels=16,
                kernel_size=3,
                stride=1,
                padding=0,
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)    #   16*48*498  ->  16*24*249
        )
        self.conv2 = nn.Sequential(         #   16*24*249  ->  32*22*247
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                stride=1,
                padding=0
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)  #    32*22*247  ->32*11*123
        )

        self.conv3 = nn.Sequential(         #   32*11*124   ->   64*9*122
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=0
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)  #  64*9*122   ->   64*4*60
        )


        self.fc1 = nn.Sequential(
            nn.Linear(in_features=64*4*60, out_features=128),
            nn.ReLU()
        )
        #
        self.fc2 = nn.Sequential(
            nn.Linear(in_features=10, out_features=64),
            nn.ReLU()
        )
        self.fc3 = nn.Sequential(
            nn.Linear(in_features=192, out_features=2),
        )

    def forward_once(self,x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(x.size(0), -1)
        c = self.fc1(x)
        return c

    def forward(self,normal,tumor,sup_feature):
        n_output=self.forward_once(normal)
        t_output=self.forward_once(tumor)
        dis=torch.abs(n_output-t_output)
        sup=self.fc2(sup_feature)
        combined = torch.cat((sup.view(sup.size(0), -1), dis.view(dis.size(0), -1)), dim=1)
        ret=self.fc3(combined)
        # ret=self.fc2(dis)
        return ret
