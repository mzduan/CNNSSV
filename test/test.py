import numpy as np
from PIL import Image
from skimage import transform
import matplotlib.pyplot as plt
if __name__ == '__main__':
    a=np.array([1,2,3,4,5])
    b = np.array([5, 2, 3, 4, 5])
    print(abs(a-b))