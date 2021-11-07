import torch
import torch.nn as nn
if __name__ == '__main__':

    # x_input=torch.randn(1,2)#随机生成输入
    # x_input = torch.randn(3, 3)  # 随机生成输入
    x_input=torch.tensor([[3.6375, -3.9186]])
    print('x_input:\n',x_input)
    y_target=torch.tensor([0])#设置输出具体值 print('y_target\n',y_target)

    #计算输入softmax，此时可以看到每一行加到一起结果都是1
    softmax_func=nn.Softmax(dim=1)
    soft_output=softmax_func(x_input)
    print('soft_output:\n',soft_output)

    #在softmax的基础上取log
    log_output=torch.log(soft_output)
    print('log_output:\n',log_output)
    #pytorch中关于NLLLoss的默认参数配置为：reducetion=True、size_average=True
    nllloss_func=nn.NLLLoss()
    nlloss_output=nllloss_func(log_output,y_target)
    print('nlloss_output:\n',nlloss_output)

    #直接使用pytorch中的loss_func=nn.CrossEntropyLoss()看与经过NLLLoss的计算是不是一样
    crossentropyloss=nn.CrossEntropyLoss()
    crossentropyloss_output=crossentropyloss(x_input,y_target)
    print('crossentropyloss_output:\n',crossentropyloss_output)
