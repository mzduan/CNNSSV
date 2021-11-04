import numpy as np
if __name__ == '__main__':
    n_feature = np.zeros((3, 50, 500))
    normal = np.load('/home/duan/Desktop/test/chr20_DEL_62150_1688/normal.npy')
    print(n_feature[0].shape)