import numpy as np
import CNN
import torch
if __name__ == '__main__':
    model_path='/Users/duan/Desktop/getBreakpoint/model/CNN_without_sup.model'
    cnn = CNN.CNN()
    cnn.load_state_dict(torch.load(model_path))


