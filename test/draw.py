import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.legend import Legend
if __name__ == '__main__':

#绘制点状图

    # x=[0.2,0.5,0.7]
    # CNNSSV_recall=[0.242,0.269,0.255]
    # sniffles_recall=[0.182,0.143,0.145]
    # cutesv_recall=[0.209,0.178,0.160]
    # nanomonsv_recall=[0.132,0.158,0.159]
    # # manta_recall=[0.143,0.387,0.496]
    # plt.scatter(x, CNNSSV_recall, s=10,c='r',label='CNNSSV')
    # plt.scatter(x, sniffles_recall, s=10, c='g',label='sniffles')
    # plt.scatter(x, cutesv_recall, s=10, c='b',label='cutesv')
    # plt.scatter(x, nanomonsv_recall, s=10,c='y',label='nanomonsv')
    # # plt.scatter(x, manta_recall, s=20,c='m',label='manta')
    # plt.legend(loc='upper left')
    # plt.xlabel("purity", fontsize=12)
    # plt.ylabel("f1-score", fontsize=22)
    # plt.ylim(0,1)
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/f1——ccs.png')
    # plt.close()
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


    #纯合模拟数据
    # plt.figure(figsize=(20,8))
    # x_read_depth = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]
    #
    # CNNSSV_recall = [0.916,0.942,0.946,0.946,0.95,0.948,0.944]
    # cutesv_recall = [0.91,0.936,0.938,0.942,0.94,0.944,0.94]
    # sniffles_recall = [0.9,0.93,0.928,0.936,0.932,0.94,0.932]
    # nanomonsv_recall = [0.24,0.276,0.288,0.298,0.312,0.34,0.34]
    #
    # CNNSSV_precision = [0.997, 0.989,0.995,0.993,0.989,0.991,0.989]
    # cutesv_precision = [0.952,0.956,0.946,0.953,0.960,0.949,0.957]
    # sniffles_precision = [0.834,0.834,0.809,0.812,0.788,0.800,0.797]
    # nanomonsv_precision = [1.0,0.992,1.0,1.0,0.993,1.0,1.0]
    #
    # CNNSSV_f1=[0.955,0.965,0.970,0.969,0.969,0.969,0.966]
    # cutesv_f1=[0.930,0.946,0.942,0.947,0.950,0.946,0.948]
    # sniffles_f1=[0.866,0.879,0.864,0.869,0.854,0.864,0.859]
    # nanomonsv_f1=[0.387,0.431,0.447,0.459,0.474,0.507,0.507]
    #
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # plt.xticks(np.arange(0.2,0.8,0.1))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/simulate.png')
    # plt.close()




    #杂合模拟数据
    # plt.figure(figsize=(20,8))
    # x_read_depth = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]
    #
    # CNNSSV_recall = [0.792,0.89,0.926,0.938,0.936,0.94,0.944]
    # cutesv_recall = [0.78,0.874,0.914,0.934,0.932,0.932,0.938]
    # sniffles_recall = [0.776,0.876,0.91,0.924,0.922,0.92,0.926]
    # nanomonsv_recall = [0.142,0.21,0.24,0.27,0.284,0.276,0.298]
    #
    # CNNSSV_precision = [0.994,0.995,0.995,0.995,0.991,0.993,0.995]
    # cutesv_precision = [0.959,0.955,0.968,0.969,0.946,0.962,0.946]
    # sniffles_precision = [0.860,0.863,0.861,0.858,0.827,0.847,0.803]
    # nanomonsv_precision = [1.0,1.0,1.0,1.0,1.0,1.0,0.993]
    #
    # CNNSSV_f1=[0.881,0.939,0.959,0.966,0.962,0.966,0.969]
    # cutesv_f1=[0.860,0.912,0.940,0.951,0.939,0.947,0.942]
    # sniffles_f1=[0.815,0.869,0.885,0.890,0.872,0.882,0.860]
    # nanomonsv_f1=[0.248,0.347,0.387,0.425,0.442,0.432,0.458]
    #
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # plt.xticks(np.arange(0.2,0.8,0.1))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/heter_simulate.png')
    # plt.close()

#绘制柱状图

    # plt.figure(figsize=(20,10))
    # name_list = ['0.2', '0.5', '0.7']
    # CNNSSV_recall = [0.781,0.845,0.845]
    # cutesv_recall = [0.836,0.881,0.9]
    # sniffles_recall = [0.718,0.690,0.718]
    # nanomonsv_recall = [0.254,0.290,0.3]
    # manta_recall=[0.08,0.281,0.390]
    #
    # CNNSSV_precision = [0.943,0.909,0.909]
    # cutesv_precision = [0.717,0.783,0.768]
    # sniffles_precision = [0.353,0.318,0.343]
    # nanomonsv_precision = [0.818,0.888,0.842]
    # manta_precision=[0.692,0.632,0.728]
    #
    # CNNSSV_f1 = [0.854,0.876,0.876]
    # cutesv_f1= [0.772,0.829,0.828]
    # sniffles_f1 = [0.473,0.436,0.464]
    # nanomonsv_f1 = [0.388,0.438,0.442]
    # manta_f1=[0.146,0.389,0.508]
    #
    # x = list(range(len(CNNSSV_recall)))
    # total_width, n = 0.8, 5
    # width = total_width / n
    #
    # plt.subplot(131)
    # plt.ylim(0, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.bar(x, CNNSSV_f1, width=width, label='CNNSSV', fc='y')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, cutesv_f1, width=width, label='cutesv', fc='r')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, nanomonsv_f1, width=width, label='nanomonsv', fc='b')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, manta_f1, width=width, label='manta', fc='c')
    #
    # plt.subplot(132)
    # plt.ylim(0, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Precision", fontsize=12)
    # plt.bar(x, CNNSSV_precision, width=width, label='CNNSSV', fc='y')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, cutesv_precision, width=width, label='cutesv', fc='r')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, sniffles_precision, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, nanomonsv_precision, width=width, label='nanomonsv', fc='b')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, manta_precision, width=width, label='manta', fc='c')
    #
    # plt.subplot(133)
    # plt.ylim(0, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.bar(x, CNNSSV_recall, width=width, label='CNNSSV', fc='y')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, cutesv_recall, width=width, label='cutesv',fc='r')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, sniffles_recall, width=width, label='sniffles', tick_label=name_list,fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, nanomonsv_recall, width=width, label='nanomonsv', fc='b')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, manta_recall, width=width, label='manta', fc='c')
    # plt.legend(loc='lower right', bbox_to_anchor=(1.32, 0))
    # plt.savefig('/Users/duan/Desktop/random.png')


    #纯合模拟数据 tumor样本测序深度发生变化时的结果，purity=0.2
    # plt.figure(figsize=(18,8))
    # x_read_depth = [10,15,20,25,30,35]
    #
    # CNNSSV_recall = [0.816,0.874,0.916,0.932,0.934,0.936]
    # cutesv_recall = [0.8,0.87,0.91,0.918,0.932,0.94]
    # sniffles_recall = [0.798,0.856,0.9,0.92,0.922,0.936]
    # nanomonsv_recall = [0.136,0.206,0.24,0.264,0.282,0.284]
    #
    # CNNSSV_precision = [0.997,0.995,0.997,0.995,0.995,0.995]
    # cutesv_precision = [0.943,0.963,0.952,0.957,0.959,0.948]
    # sniffles_precision = [0.892,0.873,0.834,0.850,0.814,0.826]
    # nanomonsv_precision = [1.0,1.0,1.0,1.0,1.0,1.0]
    #
    # CNNSSV_f1=[0.897,0.930,0.955,0.962,0.963,0.964]
    # cutesv_f1=[0.865,0.914,0.930,0.937,0.945,0.944]
    # sniffles_f1=[0.842,0.864,0.866,0.883,0.864,0.878]
    # nanomonsv_f1=[0.239,0.341,0.387,0.417,0.439,0.442]
    #
    #
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("read depth", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # plt.xticks(np.arange(10,36,5))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read depth", fontsize=12)
    # plt.ylabel("Precsion", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right')
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read depth", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/tumor_vary_depth.png')
    # plt.close()


    # 杂合模拟数据，normal样本测序深度发生变化时precision的和F1的变化
    plt.figure(figsize=(19,8))
    x_read_depth = [5,10,15,20,25]

    CNNSSV_precision = [0.885,0.987,0.994,0.994,0.994]
    cutesv_precision = [0.845,0.946,0.957,0.959,0.954]
    sniffles_precision = [0.756,0.832,0.850,0.860,0.852]
    nanomonsv_precision = [0.752,.972,1.0,1.0,1.0]

    CNNSSV_f1=[0.835,0.881,0.883,0.881,0.880]
    cutesv_f1=[0.811,0.855,0.859,0.860,0.858]
    sniffles_f1=[0.766,0.803,0.811,0.815,0.812]
    nanomonsv_f1=[0.236,0.244,0.248,0.248,0.239]

    plt.subplot(121)
    plt.ylim(0.5,1)
    plt.xlabel("read depth", fontsize=18)
    plt.ylabel("Precision", fontsize=18)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_precision,'o-',label='CNNSSV',color='r',)
    plt.plot(x_read_depth, cutesv_precision,'o-',label='cutesv',color='g')
    plt.plot(x_read_depth, sniffles_precision,'o-',label='sniffles',color='b')
    plt.plot(x_read_depth, nanomonsv_precision,'o-',label='nanomonsv',color='y')
    plt.xticks(np.arange(5,26,5))
    plt.yticks(np.arange(0.00,1.01,0.25))

    plt.subplot(122)
    plt.ylim(0.5, 1)
    plt.xlabel("read depth", fontsize=18)
    plt.ylabel("F1-score", fontsize=18)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    plt.xticks(np.arange(5, 26, 5))
    plt.yticks(np.arange(0.00, 1.01, 0.25))

    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0),prop={'size': 14})
    plt.savefig('/Users/duan/Desktop/heter_normal_vary_depth.png')
    plt.close()



    #杂合模拟数据，tumor样本测序深度发生变化时recall的和F1的变化
    plt.figure(figsize=(19,8))
    x_read_depth = [10,15,20,25,30,35]

    CNNSSV_recall = [0.566,0.688,0.786,0.848,0.866,0.894]
    cutesv_recall = [0.55,0.686,0.78,0.85,0.876,0.9]
    sniffles_recall = [0.56,0.674,0.776,0.84,0.876,0.89]
    nanomonsv_recall = [0.046,0.098,0.142,0.166,0.194,0.224]

    CNNSSV_f1=[0.721,0.811,0.878,0.913,0.927,0.944]
    cutesv_f1=[0.699,0.802,0.860,0.896,0.914,0.928]
    sniffles_f1=[0.685,0.763,0.815,0.856,0.857,0.868]
    nanomonsv_f1=[0.087,0.178,0.248,0.284,0.324,0.365]

    plt.subplot(121)
    plt.ylim(0.5,1)
    plt.xlabel("read depth", fontsize=18)
    plt.ylabel("Recall", fontsize=18)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    plt.xticks(np.arange(10,36,5))
    plt.yticks(np.arange(0.00,1.01,0.25))

    plt.subplot(122)
    plt.ylim(0.5, 1)
    plt.xlabel("read depth", fontsize=18)
    plt.ylabel("F1-score", fontsize=18)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    plt.xticks(np.arange(10, 36, 5))
    plt.yticks(np.arange(0.00, 1.01, 0.25))

    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0),prop={'size': 14})
    plt.savefig('/Users/duan/Desktop/heter_tumor_vary_depth.png')
    plt.close()

# 绘制柱状图，NA19238和NA19239混合
#     plt.figure(figsize=(20,10))
#     name_list = ['0.2', '0.5', '0.7']
#     CNNSSV_recall = [0.464,0.484,0.504]
#     cutesv_recall = [0.496,0.556,0.549]
#     sniffles_recall = [0.423,0.476,0.509]
#     nanomonsv_recall = [0.132,0.178,0.178]
#
#     # CNNSSV_precision = [0.3897,0.2995,0.2812]
#     CNNSSV_precision = [0.582,0.589,0.572]
#     cutesv_precision = [0.164,0.111,0.098]
#     sniffles_precision = [0.138,0.110,0.111]
#     nanomonsv_precision = [0.809,0.609,0.520]
#
#     # CNNSSV_f1 = [0.373,0.330,0.325]
#     CNNSSV_f1=[0.516,0.531,0.535]
#     cutesv_f1= [0.247,0.185,0.166]
#     sniffles_f1 = [0.208,0.179,0.183]
#     nanomonsv_f1 = [0.227,0.276,0.266]
#
#     x = list(range(len(CNNSSV_recall)))
#     total_width, n = 0.8, 4
#     width = total_width / n
#     plt.subplot(131)
#     plt.ylim(0, 1)
#     plt.yticks(np.arange(0.00,1.01,0.25))
#     plt.xlabel("Purity", fontsize=12)
#     plt.ylabel("F1-score", fontsize=12)
#     plt.bar(x, CNNSSV_f1, width=width, label='CNNSSV', fc='y')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, cutesv_f1, width=width, label='cutesv', fc='r')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, nanomonsv_f1, width=width, label='nanomonsv', fc='b')
#     # for i in range(len(x)):
#     #     x[i] = x[i] + width
#     # plt.bar(x, manta_f1, width=width, label='manta', fc='c')
#     # plt.legend(loc=2, bbox_to_anchor=(1.05, 1))
#
#     plt.subplot(132)
#     plt.ylim(0, 1)
#     plt.yticks(np.arange(0.00,1.01,0.25))
#     plt.xlabel("Purity", fontsize=12)
#     plt.ylabel("Precision", fontsize=12)
#     plt.bar(x, CNNSSV_precision, width=width, label='CNNSSV', fc='y')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, cutesv_precision, width=width, label='cutesv', fc='r')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, sniffles_precision, width=width, label='sniffles', tick_label=name_list, fc='g')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, nanomonsv_precision, width=width, label='nanomonsv', fc='b')
#     # for i in range(len(x)):
#     #     x[i] = x[i] + width
#     # plt.bar(x, manta_precision, width=width, label='manta', fc='c')
#
#     # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
#     plt.subplot(133)
#     plt.ylim(0, 1)
#     plt.yticks(np.arange(0.00,1.01,0.25))
#     plt.xlabel("Purity", fontsize=12)
#     plt.ylabel("Recall", fontsize=12)
#     plt.bar(x, CNNSSV_recall, width=width, label='CNNSSV', fc='y')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, cutesv_recall, width=width, label='cutesv',fc='r')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, sniffles_recall, width=width, label='sniffles', tick_label=name_list,fc='g')
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, nanomonsv_recall, width=width, label='nanomonsv', fc='b')
#     # for i in range(len(x)):
#     #     x[i] = x[i] + width
#     # plt.bar(x, manta_recall, width=width, label='manta', fc='c')
#     # plt.legend(loc=2,bbox_to_anchor=(1.05,1))
#     # plt.legend(loc='lower center')
#     plt.legend(loc='lower right', bbox_to_anchor=(1.32, 0))
#
#
#     # plt.show()
#     plt.savefig('/Users/duan/Desktop/NA9238_NA19239.png')



#绘制折线图
    #纯合模拟数据，support read由1变化到6时，各方法准确率的变化
    # plt.figure(figsize=(20,8))
    # x_read_depth = [1,2,3,4,5,6]
    #
    # CNNSSV_recall = [0.91,0.842,0.706,0.486,0.316,0.19]
    # cutesv_recall = [0.91,0.848,0.708,0.488,0.316,0.188]
    # sniffles_recall = [0.9,0.826,0.674,0.464,0.298,0.176]
    # nanomonsv_recall = [0.24,0.212,0.17,0.12,0.08,0.04]
    #
    # CNNSSV_precision = [0.997,0.997,1.0,1.0,1.0,1.0]
    # cutesv_precision = [0.952,0.962,0.968,0.963,0.958,0.964]
    # sniffles_precision = [0.834,0.945,0.971,0.978,0.973,0.956]
    # nanomonsv_precision = [1.0,1.0,1.0,1.0,1.0,1.0]
    #
    # CNNSSV_f1=[0.951,0.913,0.827,0.654,0.480,0.319]
    # cutesv_f1=[0.930,0.901,0.818,0.647,0.475,0.314]
    # sniffles_f1=[0.866,0.881,0.795,0.629,0.456,0.297]
    # nanomonsv_f1=[0.387,0.349,0.290,0.214,0.148,0.076]
    #
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00,1.1,0.25))
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.25))
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.25))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/tumor_support_read.png')
    # plt.close()
    #
    #
    #
    # #杂合模拟数据，support reads由1变化到6
    # plt.figure(figsize=(20,8))
    # x_read_depth = [1,2,3,4,5,6]
    #
    # CNNSSV_recall = [0.786,0.522, 0.274 ,0.132, 0.052 ,0.018]
    # cutesv_recall = [0.78 ,0.526, 0.274, 0.132, 0.054, 0.018]
    # sniffles_recall = [0.776 ,0.508 ,0.27 ,0.13 ,0.046 ,0.018 ]
    # nanomonsv_recall = [0.142 ,0.132, 0.072, 0.032, 0.012, 0.002 ]
    #
    # CNNSSV_precision = [0.994,1.0,1.0,1.0,1.0,1.0]
    # cutesv_precision = [0.959 ,0.963 ,0.963 ,0.936 ,0.933, 0.818]
    # sniffles_precision = [0.860 ,0.940, 0.9507 ,0.902 ,0.821,0.642]
    # nanomonsv_precision = [1.0,1.0,1.0,1.0,1.0,1.0]
    #
    # CNNSSV_f1=[0.878,0.685 ,0.4301, 0.233 ,0.098, 0.035 ]
    # cutesv_f1=[0.860 ,0.680 ,0.426, 0.231 ,0.102 ,0.035 ]
    # sniffles_f1=[0.815 ,0.659 ,0.420 ,0.227 ,0.087 ,0.035]
    # nanomonsv_f1=[0.248 ,0.233, 0.134 ,0.062 ,0.023 ,0.003]
    #
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00,1.1,0.25))
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.25))
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.25))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/heter_tumor_support_read.png')
    # plt.close()



#绘制全染色体模拟数据上，FP的情况
    # plt.figure(figsize=(20,10))
    # name_list = ['CNNSSV','cutesv','sniffles']
    # DEL = [85,411,1082]
    # INS = [480,588,354]
    # INV = [21,98,251]
    # DUP = [460,1583,723]
    #
    # x = list(range(len(DEL)))
    # total_width, n = 0.8, 4
    # width = total_width / n
    # plt.ylim(0, 1600)
    # plt.ylabel("FP Counts", fontsize=12)
    # plt.bar(x, DEL, width=width, label='DEL', fc='y')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, INS, width=width, label='INS', tick_label=name_list,fc='r')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, INV, width=width, label='INV', fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, DUP, width=width, label='DUP', fc='b')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/random_FP.png')

# 绘制全染色体模拟数据上的结果，点状图

    # plt.figure(figsize=(20,10))
    # CNNSSV_recall_2=0.781
    # CNNSSV_precision_2=0.943
    # CNNSSV_recall_5=0.845
    # CNNSSV_precision_5=0.909
    # CNNSSV_recall_7 = 0.850
    # CNNSSV_precision_7 = 0.904
    #
    # cutesv_recall_2 = 0.836
    # cutesv_precision_2 = 0.717
    # cutesv_recall_5 = 0.881
    # cutesv_precision_5 = 0.783
    # cutesv_recall_7 = 0.9
    # cutesv_precision_7 = 0.768
    #
    # sniffles_recall_2 = 0.7181
    # sniffles_precision_2 = 0.35
    # sniffles_recall_5 = 0.69
    # sniffles_precision_5 = 0.31
    # sniffles_recall_7 = 0.718
    # sniffles_precision_7 = 0.33
    #
    # nano_recall_2 = 0.081
    # nano_precision_2 = 0.69
    # nano_recall_5 = 0.28
    # nano_precision_5 = 0.63
    # nano_recall_7 = 0.39
    # nano_precision_7 = 0.72
    #
    # # manta_recall=[0.143,0.387,0.496]
    # plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=10,c='',edgecolors='black',label="purity=0.2")
    # plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=10,c='',edgecolors='black',marker='^',label="purity=0.5")
    # plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=10,c='',edgecolors='black',marker='s',label="purity=0.7")
    #
    # plt.scatter(cutesv_recall_2, cutesv_precision_2, s=10, c='g')
    # plt.scatter(cutesv_recall_5, cutesv_precision_5, s=10, c='g', marker='^')
    # plt.scatter(cutesv_recall_7, cutesv_precision_7, s=10, c='g', marker='s')
    #
    # plt.scatter(sniffles_recall_2, sniffles_precision_2, s=10, c='b')
    # plt.scatter(sniffles_recall_5, sniffles_precision_5, s=10, c='b', marker='^')
    # plt.scatter(sniffles_recall_7, sniffles_precision_7, s=10, c='b', marker='s')
    #
    # plt.scatter(nano_recall_2, nano_precision_2, s=10, c='c')
    # plt.scatter(nano_recall_5, nano_precision_5, s=10, c='c', marker='^')
    # plt.scatter(nano_recall_7, nano_precision_7, s=10, c='c', marker='s')
    #
    # plt.scatter(0.5, 0.5, s=0, c='b', marker='s')
    # # plt.scatter(x, manta_recall, s=20,c='m',label='manta')
    # # plt.legend(["0.2","0.5","0.7"])
    # plt.xlabel("recall", fontsize=12)
    # plt.ylabel("precision", fontsize=12)
    # plt.xlim(0,1)
    # plt.ylim(0,1)
    # # plt.show()
    # method_labels = ['CNNSSV', 'cutesv', 'sniffles', 'nanomonsv']
    # color = ['r', 'g', 'b', 'c']
    # # markers = ['o', '^', 's'
    # plt.legend(loc='upper left')
    # plt.savefig('/Users/duan/Desktop/random_results_1.png')
    # plt.close()



