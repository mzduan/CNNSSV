import matplotlib.pyplot as plt
if __name__ == '__main__':

#绘制recall和purity的关系

    x=[0,4,7,8,5,3,1]
    CNNSSV_recall=[0,5,8,9,6,4,1]
    # sniffles_recall=[0.804,0.810,0.893]
    # cutesv_recall=[0.892,0.899,0.949]
    # nanomonsv_recall=[0.729,0.843,0.857]
    # manta_recall=[0.143,0.387,0.496]
    plt.scatter(x, CNNSSV_recall, s=10,c='r',label='CNNSSV')
    # plt.scatter(x, sniffles_recall, s=10, c='g',label='sniffles+diff')
    # plt.scatter(x, cutesv_recall, s=10, c='b',label='cutesv+diff')
    # plt.scatter(x, nanomonsv_recall, s=10,c='y',label='nanomonsv')
    # plt.scatter(x, manta_recall, s=20,c='m',label='manta')
    plt.legend(loc='lower right')
    plt.xlabel("purity", fontsize=12)
    plt.ylabel("f1-score", fontsize=22)
    plt.ylim(-10,10)
    # plt.show()
    plt.savefig('/Users/duan/Desktop/f1——clr.png')
    plt.close()
#绘制precision和purity的关系
    # x = [0.2, 0.5, 0.7]
    # CNNSSV_precision=[0.996,0.994,0.987]
    # sniffles_precision=[0.816, 0.804, 0.800]
    # cutesv_precision=[0.962, 0.951, 0.953]
    # nanomonsv_precision=[0.997,0.997,0.995]
    # plt.scatter(x, CNNSSV_precision, s=50, c='r', label='CNNSSV')
    # plt.scatter(x, sniffles_precision, s=50, c='g', label='sniffles+diff')
    # plt.scatter(x, cutesv_precision, s=50, c='b', label='cutesv+diff')
    # plt.scatter(x, nanomonsv_precision, s=20,c='y',label='nanomonsv')
    # plt.legend(loc='lower right')
    # plt.xlabel("purity", fontsize=12)
    # plt.ylabel("precision", fontsize=22)
    # plt.ylim(0.5,1)
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/precision.png')


#绘制折线图
    # x = [5, 10,15,20]
    # y1 = [0.804, 0.807, 0.820, 0.817]
    #
    # y2 = [0.960, 0.962, 0.968, 0.966]
    # y3 = [0.984, 0.995, 0.997, 0.996]
    #
    #
    # plt.ylim(0.5,1)
    # plt.xlabel("normal sequence depth", fontsize=12)
    # plt.ylabel("precision", fontsize=22)
    # plt.plot(x, y1,label='sniffles',color='r')
    # plt.plot(x, y2,label='cutes',color='g')
    # plt.plot(x, y3,label='CNNSSV',color='b')
    # plt.legend()
    # plt.savefig('/Users/duan/Desktop/precision.png')

