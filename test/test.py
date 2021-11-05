import numpy as np
import torch
if __name__ == '__main__':
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.empty(3, dtype=torch.long).random_(5)
    print(input)
    print(target)
    print(target.shape)