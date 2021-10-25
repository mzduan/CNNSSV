import torch
import torch.nn as nn
import Siamese
import SiameseTrainNetworkDataset
import sys
from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter
epoches = 4
batch_size = 4
learning_rate = 0.001
if __name__ == '__main__':

    cuda_gpu = torch.cuda.is_available()
    # cuda_gpu=False

    writer = SummaryWriter('/home/mzduan/trainlog')
    siamese= Siamese.Siamese()
    if cuda_gpu:
        siamese=siamese.cuda()
    optimizer = torch.optim.Adam(siamese.parameters(), lr=learning_rate)
    loss_function = nn.CrossEntropyLoss()

    ccs_feat_path=sys.argv[1]
    # clr_feat_path=sys.argv[2]
    model_output=sys.argv[2]


    #ccs_feat_path = '/home/duan/Desktop/train'
    #model_output='/home/duan/Desktop/test.model'


    train_set=SiameseTrainNetworkDataset.SiameseTrainNetworkDataset(ccs_feat_path)
    train_loader=DataLoader(train_set,batch_size=4,shuffle=True)
    # 开始训练
    for epoch in range(epoches):
        print("进行第{}个epoch".format(epoch))
        for step, (batch_n,batch_t, batch_sup,batch_y) in enumerate(train_loader):
            if cuda_gpu:
                batch_n=batch_n.cuda()
                batch_t=batch_t.cuda()
                batch_sup_x=batch_sup_x.cuda()
                batch_y = batch_y.cuda()
            output = siamese(batch_n,batch_t,batch_sup)
            loss = loss_function(output, batch_y)

            writer.add_scalar("Train Loss", loss.data.item(), epoch * len(train_set) + step)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 为了实时显示准确率
            if step % 100 == 0:
                print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.cpu().numpy())

    siamese=siamese.cpu()
    torch.save(siamese.state_dict(),model_output)
