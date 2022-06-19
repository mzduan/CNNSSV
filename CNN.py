import torch.nn as nn
import torch
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(    # 6*50*500  ->   16*48*498
            nn.Conv2d(
                in_channels=6,
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

        #处理image的fc
        self.fc1 = nn.Sequential(
            nn.Linear(in_features=64*4*60, out_features=8),
            nn.ReLU()
        )

        #处理vector的fc
        self.fc2=nn.Sequential(
            nn.Linear(in_features=18, out_features=4),
            nn.ReLU()
        )

        #处理融合后的特征
        self.fc3=nn.Sequential(
            nn.Linear(in_features=12, out_features=2),
            # nn.ReLU()
        )

    def forward(self, x,sup_x):

        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(x.size(0), -1)
        c = self.fc1(x)
        f = self.fc2(sup_x)
        combined=torch.cat((c.view(c.size(0), -1),f.view(f.size(0), -1)), dim=1)
        final_output=self.fc3(combined)
        return final_output
