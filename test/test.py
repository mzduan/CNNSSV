import numpy as np
if __name__ == '__main__':
    n_feat=np.load('/home/duan/Desktop/test/chr20_DEL_709833_92/normal_sup_feature.npy')
    t_feat=np.load('/home/duan/Desktop/test/chr20_DEL_709833_92/tumor_sup_feature.npy')

    print(n_feat)
    print(t_feat)


