import numpy as np
if __name__ == '__main__':
    a=[1,2,3,4,5]
    for i in range(len(a)):
        a[i]=a[i]/5

    b=np.array(a,dtype=int)
    print(b)