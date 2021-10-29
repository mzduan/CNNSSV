import numpy as np
from PIL import Image
from skimage import transform
import matplotlib.pyplot as plt
if __name__ == '__main__':
    a=[1,2,3,4,5]
    for i in range(len(a)):
        a[i]=a[i]/7
    print(a)