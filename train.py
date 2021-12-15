import torch
import torch.nn as nn
import CNN
import TrainSet
import sys
from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter
epoches = 4
batch_size = 4
learning_rate = 0.0005
if __name__ == '__main__':

    cuda_gpu = torch.cuda.is_available()
    # cuda_gpu=False

    writer = SummaryWriter('/home/mzduan/somaticSV/model/trainlog_CNN_sup_with_confusion_normal')
    cnn=CNN.CNN()
    if cuda_gpu:
        cnn=cnn.cuda()
    optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)
    loss_function = nn.CrossEntropyLoss()

    ccs_feat_path=sys.argv[1]
    # clr_feat_path=sys.argv[2]
    model_output=sys.argv[2]


    # feat_path = '/Users/duan/Desktop/results/somaticSV/features'
    # model_output='/Users/duan/Desktop/cnn.model'


    train_set=TrainSet.TrainSet(ccs_feat_path)
    train_loader=DataLoader(train_set,batch_size=4,shuffle=True)
    # 开始训练
    for epoch in range(epoches):
        print("进行第{}个epoch".format(epoch))
        for step, (batch_x,batch_sup_x,batch_y) in enumerate(train_loader):
            if cuda_gpu:
                batch_x=batch_x.cuda()
                batch_sup_x = batch_sup_x.cuda()
                batch_y = batch_y.cuda()
            output = cnn(batch_x,batch_sup_x)
            loss = loss_function(output, batch_y)

            writer.add_scalar("Train Loss", loss.data.item(), epoch * len(train_set) + step)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 为了实时显示准确率
            if step % 100 == 0:
                print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.cpu().numpy())

    cnn=cnn.cpu()
    torch.save(cnn.state_dict(),model_output)

