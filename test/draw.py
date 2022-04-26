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
    plt.figure(figsize=(20,8))
    x_read_depth = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]

    CNNSSV_recall = [0.916,0.942,0.946,0.946,0.95,0.948,0.944]
    cutesv_recall = [0.91,0.936,0.938,0.942,0.94,0.944,0.94]
    sniffles_recall = [0.9,0.93,0.928,0.936,0.932,0.94,0.932]
    nanomonsv_recall = [0.24,0.276,0.288,0.298,0.312,0.34,0.34]

    CNNSSV_precision = [0.997, 0.989,0.995,0.993,0.989,0.991,0.989]
    cutesv_precision = [0.952,0.956,0.946,0.953,0.960,0.949,0.957]
    sniffles_precision = [0.834,0.834,0.809,0.812,0.788,0.800,0.797]
    nanomonsv_precision = [1.0,0.992,1.0,1.0,0.993,1.0,1.0]

    CNNSSV_f1=[0.955,0.965,0.970,0.969,0.969,0.969,0.966]
    cutesv_f1=[0.930,0.946,0.942,0.947,0.950,0.946,0.948]
    sniffles_f1=[0.866,0.879,0.864,0.869,0.854,0.864,0.859]
    nanomonsv_f1=[0.387,0.431,0.447,0.459,0.474,0.507,0.507]

    plt.subplot(131)
    plt.ylim(0.5, 1)
    plt.xlabel("Purity", fontsize=18)
    plt.ylabel("F1-score", fontsize=18)
    # plt.grid()
    ax = plt.gca()  # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', lw=1, markersize=4)
    plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g', lw=1, markersize=4)
    plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b', lw=1, markersize=4)
    plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y', lw=1, markersize=4)
    plt.xticks(np.arange(0.2, 0.8, 0.1))
    plt.yticks(np.arange(0.2, 1.01, 0.1))
    plt.tick_params(labelsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("(a)F1-score随肿瘤纯度纯度变化",y=-0.14)

    plt.subplot(132)
    plt.ylim(0.5,1)
    plt.xlabel("Purity", fontsize=18)
    plt.ylabel("Recall", fontsize=18)
    # plt.grid()
    ax = plt.gca()  # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g',lw=1,markersize=4)
    plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b',lw=1,markersize=4)
    plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    plt.xticks(np.arange(0.2,0.8,0.1))
    plt.yticks(np.arange(0.2,1.01,0.1))
    plt.tick_params(labelsize=16)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("(b)Recall随肿瘤纯度纯度变化",y=-0.2)

    plt.subplot(133)
    plt.ylim(0.5, 1)
    plt.xlabel("Purity", fontsize=18)
    plt.ylabel("Precsion", fontsize=18)
    # plt.grid()
    ax = plt.gca()  # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r',lw=1,markersize=4)
    plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g',lw=1,markersize=4)
    plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b',lw=1,markersize=4)
    plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y',lw=1,markersize=4)
    plt.xticks(np.arange(0.2, 0.8, 0.1))
    plt.yticks(np.arange(0.2, 1.01, 0.1))
    plt.tick_params(labelsize=16)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("(c)Precision随肿瘤纯度纯度变化",y=-0.1)

    plt.xticks(np.arange(0.2, 0.8, 0.1))
    plt.yticks(np.arange(0.2, 1.01, 0.1))
    plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    plt.tick_params(labelsize=16)
    plt.savefig('/Users/duan/Desktop/simulate.png')
    plt.close()




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
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', lw=1, markersize=4)
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g', lw=1, markersize=4)
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b', lw=1, markersize=4)
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y', lw=1, markersize=4)
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.1))
    # plt.tick_params(labelsize=16)
    #
    #
    # plt.subplot(132)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(0.2,0.8,0.1))
    # plt.yticks(np.arange(0.00,1.01,0.1))
    # plt.tick_params(labelsize=16)
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r',lw=1,markersize=4 )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.1))
    # plt.tick_params(labelsize=16)
    #
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
    # plt.figure(figsize=(19,8))
    # x_read_depth = [5,10,15,20,25]
    #
    # CNNSSV_precision = [0.885,0.987,0.994,0.994,0.994]
    # cutesv_precision = [0.845,0.946,0.957,0.959,0.954]
    # sniffles_precision = [0.756,0.832,0.850,0.860,0.852]
    # nanomonsv_precision = [0.752,.972,1.0,1.0,1.0]
    #
    # CNNSSV_f1=[0.835,0.881,0.883,0.881,0.880]
    # cutesv_f1=[0.811,0.855,0.859,0.860,0.858]
    # sniffles_f1=[0.766,0.803,0.811,0.815,0.812]
    # nanomonsv_f1=[0.236,0.244,0.248,0.248,0.239]
    #
    # plt.subplot(121)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read depth", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', lw=1, markersize=4)
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g', lw=1, markersize=4)
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b', lw=1, markersize=4)
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y', lw=1, markersize=4)
    # plt.xticks(np.arange(5, 26, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.10))
    # plt.tick_params(labelsize=16)
    #
    #
    #
    # plt.subplot(122)
    # plt.ylim(0.5,1)
    # plt.xlabel("read depth", fontsize=18)
    # plt.ylabel("Precision", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_precision,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_precision,'o-',label='cutesv',color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_precision,'o-',label='sniffles',color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_precision,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(5,26,5))
    # plt.yticks(np.arange(0.00,1.01,0.10))
    # plt.tick_params(labelsize=16)
    #
    #
    # plt.legend(loc='lower right', bbox_to_anchor=(1.29, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/heter_normal_vary_depth.png')
    # plt.close()
    #
    #
    #
    # #杂合模拟数据，tumor样本测序深度发生变化时recall的和F1的变化
    # plt.figure(figsize=(19,8))
    # x_read_depth = [10,15,20,25,30,35]
    #
    # CNNSSV_recall = [0.566,0.688,0.786,0.848,0.866,0.894]
    # cutesv_recall = [0.55,0.686,0.78,0.85,0.876,0.9]
    # sniffles_recall = [0.56,0.674,0.776,0.84,0.876,0.89]
    # nanomonsv_recall = [0.046,0.098,0.142,0.166,0.194,0.224]
    #
    # CNNSSV_f1=[0.721,0.811,0.878,0.913,0.927,0.944]
    # cutesv_f1=[0.699,0.802,0.860,0.896,0.914,0.928]
    # sniffles_f1=[0.685,0.763,0.815,0.856,0.857,0.868]
    # nanomonsv_f1=[0.087,0.178,0.248,0.284,0.324,0.365]
    #
    # plt.subplot(121)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read depth", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', lw=1, markersize=4)
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g', lw=1, markersize=4)
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b', lw=1, markersize=4)
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y', lw=1, markersize=4)
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.1))
    # plt.tick_params(labelsize=16)
    #
    #
    # plt.subplot(122)
    # plt.ylim(0.5,1)
    # plt.xlabel("read depth", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(10,36,5))
    # plt.yticks(np.arange(0.00,1.01,0.1))
    # #
    # plt.tick_params(labelsize=16)
    # plt.legend(loc='lower right', bbox_to_anchor=(1.29, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/heter_tumor_vary_depth.png')
    # plt.close()

#绘制柱状图，NA19238和NA19239混合
    # plt.figure(figsize=(20,10))
    # name_list = ['0.2', '0.5', '0.7']
    # CNNSSV_recall = [0.464,0.484,0.504]
    # cutesv_recall = [0.496,0.556,0.549]
    # sniffles_recall = [0.423,0.476,0.509]
    # nanomonsv_recall = [0.132,0.178,0.178]
    #
    # # CNNSSV_precision = [0.3897,0.2995,0.2812]
    # CNNSSV_precision = [0.582,0.589,0.572]
    # cutesv_precision = [0.164,0.111,0.098]
    # sniffles_precision = [0.138,0.110,0.111]
    # nanomonsv_precision = [0.809,0.609,0.520]
    #
    # # CNNSSV_f1 = [0.373,0.330,0.325]
    # CNNSSV_f1=[0.516,0.531,0.535]
    # cutesv_f1= [0.247,0.185,0.166]
    # sniffles_f1 = [0.208,0.179,0.183]
    # nanomonsv_f1 = [0.227,0.276,0.266]
    #
    # x = list(range(len(CNNSSV_recall)))
    # total_width, n = 0.8, 4
    # width = total_width / n
    # plt.subplot(131)
    # plt.ylim(0, 1)
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # plt.tick_params(labelsize=16)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
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
    # # for i in range(len(x)):
    # #     x[i] = x[i] + width
    # # plt.bar(x, manta_f1, width=width, label='manta', fc='c')
    # # plt.legend(loc=2, bbox_to_anchor=(1.05, 1))
    #
    # plt.subplot(132)
    # plt.ylim(0, 1)
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # plt.tick_params(labelsize=16)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Precision", fontsize=18)
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
    # # for i in range(len(x)):
    # #     x[i] = x[i] + width
    # # plt.bar(x, manta_precision, width=width, label='manta', fc='c')
    #
    # # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.subplot(133)
    # plt.ylim(0, 1)
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # plt.tick_params(labelsize=16)
    # plt.xlabel("Purity", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
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
    # # for i in range(len(x)):
    # #     x[i] = x[i] + width
    # # plt.bar(x, manta_recall, width=width, label='manta', fc='c')
    # # plt.legend(loc=2,bbox_to_anchor=(1.05,1))
    # # plt.legend(loc='lower center')
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    #
    #
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/NA9238_NA19239.png')



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
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', lw=1, markersize=4)
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g', lw=1, markersize=4)
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b', lw=1, markersize=4)
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y', lw=1, markersize=4)
    # plt.xticks(np.arange(1, 6.1, 1))
    # plt.yticks(np.arange(0.00, 1.1, 0.1))
    # plt.tick_params(labelsize=16)
    #
    #
    # plt.subplot(132)
    # plt.ylim(0.5,1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00,1.1,0.1))
    # plt.tick_params(labelsize=16)
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.1))
    # plt.tick_params(labelsize=16)
    #
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/tumor_support_read.png')
    # plt.close()
    #
    #
    #
    # # 杂合模拟数据，support reads由1变化到6
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
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(1, 6.1, 1))
    # plt.yticks(np.arange(0.00, 1.1, 0.1))
    #
    # plt.tick_params(labelsize=16)
    # plt.subplot(132)
    # plt.ylim(0.5,1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Recall", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',lw=1,markersize=4)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00,1.1,0.1))
    #
    # plt.tick_params(labelsize=16)
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("min support read", fontsize=18)
    # plt.ylabel("Precsion", fontsize=18)
    # # plt.grid()
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r',lw=1,markersize=4 )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g',lw=1,markersize=4)
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b',lw=1,markersize=4)
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y',lw=1,markersize=4)
    # plt.xticks(np.arange(1,6.1,1))
    # plt.yticks(np.arange(0.00, 1.1, 0.1))
    # plt.tick_params(labelsize=16)
    #
    #
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/heter_tumor_support_read.png')
    # plt.close()

# 绘制全染色体模拟数据上的结果，点状图

    # plt.figure(figsize=(10,10))
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
    # sniffles_precision_7 = 0.34
    #
    # nano_recall_2 = 0.254
    # nano_precision_2 = 0.818
    # nano_recall_5 = 0.290
    # nano_precision_5 = 0.888
    # nano_recall_7 = 0.3
    # nano_precision_7 = 0.842
    #
    #
    # manta_recall_2 = 0.081
    # manta_precision_2 = 0.692
    # manta_recall_5 = 0.281
    # manta_precision_5 = 0.632
    # manta_recall_7 = 0.390
    # manta_precision_7 = 0.728
    #
    # manta_recall=[0.143,0.387,0.496]
    # # plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=10,c='',edgecolors='black',label="purity=0.2")
    # # plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=10,c='',edgecolors='black',marker='^',label="purity=0.5")
    # # plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=10,c='',edgecolors='black',marker='s',label="purity=0.7")
    #
    #
    # plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=50,c='r',label="CNNSSV")
    # plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=50,c='r',marker='^')
    # plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=50,c='r',marker='s')
    #
    #
    # plt.scatter(cutesv_recall_2, cutesv_precision_2, s=50, c='g',label="cutesv")
    # plt.scatter(cutesv_recall_5, cutesv_precision_5, s=50, c='g', marker='^')
    # plt.scatter(cutesv_recall_7, cutesv_precision_7, s=50, c='g', marker='s')
    #
    # plt.scatter(sniffles_recall_2, sniffles_precision_2, s=50, c='b',label="sniffles")
    # plt.scatter(sniffles_recall_5, sniffles_precision_5, s=50, c='b', marker='^')
    # plt.scatter(sniffles_recall_7, sniffles_precision_7, s=50, c='b', marker='s')
    #
    # plt.scatter(nano_recall_2, nano_precision_2, s=50, c='y',label="nanomonsv")
    # plt.scatter(nano_recall_5, nano_precision_5, s=50, c='y', marker='^')
    # plt.scatter(nano_recall_7, nano_precision_7, s=50, c='y', marker='s')
    #
    # plt.scatter(manta_recall_2, manta_precision_2, s=50, c='c',label="manta")
    # plt.scatter(manta_recall_5, manta_precision_5, s=50, c='c', marker='^')
    # plt.scatter(manta_recall_7, manta_precision_7, s=50, c='c', marker='s')
    #
    # # plt.scatter(0.5, 0.5, s=0, c='b', marker='s')
    # # plt.scatter(x, manta_recall, s=20,c='m',label='manta')
    # # plt.legend(["0.2","0.5","0.7"])
    # plt.xlabel("recall", fontsize=18)
    # plt.ylabel("precision", fontsize=18)
    # plt.xlim(0,1)
    # plt.ylim(0,1)
    # plt.tick_params(labelsize=16)
    # # plt.show()
    # # method_labels = ['CNNSSV', 'cutesv', 'sniffles', 'nanomonsv']
    # # color = ['r', 'g', 'b', 'c']
    # # markers = ['o', '^', 's'
    # plt.legend(loc='lower left',prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/random_results.png')
    # plt.close()


# # 绘制0.2~0.8 chr20 模拟数据上，FP的情况
#     plt.figure(figsize=(20,10))
#     name_list = ['DEL','INS','INV','DUP']
#     DEL = [17,28,61,0]
#     INS = [6,10,21,0]
#     INV = [1,7,305,0]
#     DUP = [1,51,371,2]
#
#     CNNSSV=[17,6,1,1]
#     cutesv=[28,10,7,51]
#     sniffles=[61,21,305,371]
#     nanomonsv=[0,0,0,2]
#
#     x = list(range(len(CNNSSV)))
#     total_width, n = 0.8, 4
#     width = total_width / n
#     plt.ylim(0, 400)
#     plt.ylabel("FP Counts", fontsize=18)
#     plt.tick_params(labelsize=16)
#     plt.bar(x, CNNSSV, width=width, label='CNNSSV', fc='r')
#     for label_x,label_y in zip(x,CNNSSV):
#         plt.text(label_x,label_y+0.05,'%.2f' %label_y, ha='center',va='bottom',size=15)
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, cutesv, width=width, label='cutesv', tick_label=name_list,fc='g')
#     for label_x, label_y in zip(x, cutesv):
#         plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, sniffles, width=width, label='sniffles', fc='b')
#     for label_x, label_y in zip(x, sniffles):
#         plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
#     for i in range(len(x)):
#         x[i] = x[i] + width
#     plt.bar(x, nanomonsv, width=width, label='nanomonsv', fc='y')
#     for label_x, label_y in zip(x, nanomonsv):
#         plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
#     plt.legend(loc='upper left',prop={'size': 16})
#     # plt.show()
#     plt.savefig('/Users/duan/Desktop/simulate_FP.png')

#绘制0.2~0.8 chr20 模拟数据上，FN的情况
    # plt.figure(figsize=(20, 10))
    # name_list = ['DEL', 'INS', 'INV', 'DUP']
    # # DEL = [17,28,61,0]
    # # INS = [6,10,21,0]
    # # INV = [1,7,305,0]
    # # DUP = [1,51,371,2]
    # CNNSSV = [31,50,44,79]
    # cutesv = [30,79,43,73]
    # sniffles = [44,78,46,83]
    # nanomonsv = [69,875,875,634]
    #
    # x = list(range(len(CNNSSV)))
    # total_width, n = 0.8, 4
    # width = total_width / n
    # plt.ylim(0, 1000)
    # plt.ylabel("FN Counts", fontsize=18)
    # plt.tick_params(labelsize=16)
    # plt.bar(x, CNNSSV, width=width, label='CNNSSV', fc='r')
    # for label_x,label_y in zip(x,CNNSSV):
    #     plt.text(label_x,label_y+0.05,'%.2f' %label_y, ha='center',va='bottom',size=15)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, cutesv, width=width, label='cutesv', tick_label=name_list, fc='g')
    # for label_x, label_y in zip(x, cutesv):
    #     plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, sniffles, width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, sniffles):
    #     plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, nanomonsv, width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, nanomonsv):
    #     plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom',size=15)
    # plt.legend(loc='upper left', prop={'size': 16})
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/simulate_FN.png')


# 绘制NA19238_NA19239真实数据上的结果，点状图

    # plt.figure(figsize=(10,10))
    # CNNSSV_recall_2=0.464
    # CNNSSV_precision_2=0.582
    # CNNSSV_recall_5=0.484
    # CNNSSV_precision_5=0.589
    # CNNSSV_recall_7 = 0.504
    # CNNSSV_precision_7 = 0.572

    # CNNSSV_recall_2 = 0.364
    # CNNSSV_precision_2 = 0.382
    # CNNSSV_recall_5 = 0.384
    # CNNSSV_precision_5 = 0.289
    # CNNSSV_recall_7 = 0.404
    # CNNSSV_precision_7 = 0.272

    # CNNSSV_recall_2 = 0.476
    # CNNSSV_precision_2 = 0.529
    # CNNSSV_recall_5 = 0.509
    # CNNSSV_precision_5 = 0.402
    # CNNSSV_recall_7 = 0.536
    # CNNSSV_precision_7 = 0.390

#     CNNSSV_recall_2=0.464
#     CNNSSV_precision_2=0.582
#     CNNSSV_recall_5=0.484
#     CNNSSV_precision_5=0.589
#     CNNSSV_recall_7 = 0.504
#     CNNSSV_precision_7 = 0.572
#
#     CNNSSV_recall_2=0.364
#     CNNSSV_precision_2=0.382
#     CNNSSV_recall_5=0.384
#     CNNSSV_precision_5=0.289
#     CNNSSV_recall_7 = 0.404
#     CNNSSV_precision_7 = 0.272

    # cutesv_recall_2 = 0.496
    # cutesv_precision_2 = 0.164
    # cutesv_recall_5 = 0.556
    # cutesv_precision_5 =0.111
    # cutesv_recall_7 = 0.549
    # cutesv_precision_7 = 0.098
    #
    # sniffles_recall_2 = 0.423
    # sniffles_precision_2 =0.138
    # sniffles_recall_5 =0.476
    # sniffles_precision_5 =0.110
    # sniffles_recall_7 = 0.509
    # sniffles_precision_7 = 0.111
    #
    # nano_recall_2 = 0.132
    # nano_precision_2 = 0.809
    # nano_recall_5 = 0.178
    # nano_precision_5 = 0.609
    # nano_recall_7 = 0.178
    # nano_precision_7 =0.520

    # plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=10,c='',edgecolors='black',label="purity=0.2")
    # plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=10,c='',edgecolors='black',marker='^',label="purity=0.5")
    # plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=10,c='',edgecolors='black',marker='s',label="purity=0.7")


    # plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=50,c='r',label="CNNSSV")
    # plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=50,c='r',marker='^')
    # plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=50,c='r',marker='s')
    #
    #
    # plt.scatter(cutesv_recall_2, cutesv_precision_2, s=50, c='g',label="cutesv")
    # plt.scatter(cutesv_recall_5, cutesv_precision_5, s=50, c='g', marker='^')
    # plt.scatter(cutesv_recall_7, cutesv_precision_7, s=50, c='g', marker='s')
    #
    # plt.scatter(sniffles_recall_2, sniffles_precision_2, s=50, c='b',label="sniffles")
    # plt.scatter(sniffles_recall_5, sniffles_precision_5, s=50, c='b', marker='^')
    # plt.scatter(sniffles_recall_7, sniffles_precision_7, s=50, c='b', marker='s')
    #
    # plt.scatter(nano_recall_2, nano_precision_2, s=50, c='y',label="nanomonsv")
    # plt.scatter(nano_recall_5, nano_precision_5, s=50, c='y', marker='^')
    # plt.scatter(nano_recall_7, nano_precision_7, s=50, c='y', marker='s')
# =======
#     plt.scatter(CNNSSV_recall_2, CNNSSV_precision_2, s=12,c='r',label="CNNSSV")
#     plt.scatter(CNNSSV_recall_5, CNNSSV_precision_5, s=12,c='r',marker='^')
#     plt.scatter(CNNSSV_recall_7, CNNSSV_precision_7, s=12,c='r',marker='s')
#
#
#     plt.scatter(cutesv_recall_2, cutesv_precision_2, s=12, c='g',label="cutesv")
#     plt.scatter(cutesv_recall_5, cutesv_precision_5, s=12, c='g', marker='^')
#     plt.scatter(cutesv_recall_7, cutesv_precision_7, s=12, c='g', marker='s')
#
#     plt.scatter(sniffles_recall_2, sniffles_precision_2, s=12, c='b',label="sniffles")
#     plt.scatter(sniffles_recall_5, sniffles_precision_5, s=12, c='b', marker='^')
#     plt.scatter(sniffles_recall_7, sniffles_precision_7, s=12, c='b', marker='s')
#
#     plt.scatter(nano_recall_2, nano_precision_2, s=12, c='c',label="nanomonsv")
#     plt.scatter(nano_recall_5, nano_precision_5, s=12, c='c', marker='^')
#     plt.scatter(nano_recall_7, nano_precision_7, s=12, c='c', marker='s')
# >>>>>>> e76c9ea36387362ee4389b25742f9a27d644f821
#
#     plt.scatter(0.5, 0.5, s=0, c='b', marker='s')
#     plt.legend(["0.2","0.5","0.7"])
# <<<<<<< HEAD
#     plt.xlabel("recall", fontsize=18)
#     plt.ylabel("precision", fontsize=18)
#     plt.xlim(0,1)
#     plt.ylim(0,1)
#     plt.tick_params(labelsize=16)
# =======
#     plt.xlabel("recall", fontsize=18)
#     plt.ylabel("precision", fontsize=18)
#     plt.tick_params(labelsize=16)
#     plt.xlim(0,1)
#     plt.ylim(0,1)
# >>>>>>> e76c9ea36387362ee4389b25742f9a27d644f821
    # plt.show()
    # method_labels = ['CNNSSV', 'cutesv', 'sniffles', 'nanomonsv']
    # color = ['r', 'g', 'b', 'c']
    # markers = ['o', '^', 's']
# <<<<<<< HEAD
#     plt.legend(loc='lower left',prop={'size': 14})
#     plt.savefig('/Users/duan/Desktop/NA19238_NA19239_plot_1.png')
# =======
#     plt.legend(loc='lower left')
#     plt.savefig('/home/duan/Desktop/NA19238_NA19239_plot_1.png')
# >>>>>>> e76c9ea36387362ee4389b25742f9a27d644f821

    # plt.close()


#画运行时间的折线图，CNNSSV与nanomonsv比较

    # plt.figure(figsize=(8,8))
    # x_read_depth = [10,15,20,25,30,35]
    #
    # CNNSSV_time=[468,478,540,609,652,626]
    # nanomonsv_time=[530,887,1313,1679,1805,2098]
    #
    # # plt.ylim(0.5,1)
    # plt.xlabel("tumor read depth", fontsize=18)
    # plt.ylabel("time(s)", fontsize=18)
    # # plt.grid()
# <<<<<<< HEAD
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.plot(x_read_depth, CNNSSV_time,'o-',label='CNNSSV',color='r')
    # for label_x,label_y in zip(x_read_depth,CNNSSV_time):
    #     plt.text(label_x,label_y+0.05,'%.2f' %label_y, ha='center',va='bottom',size=14)
    # plt.plot(x_read_depth, nanomonsv_time,'o-',label='nanomonsv',color='g')
    # for label_x, label_y in zip(x_read_depth, nanomonsv_time):
    #     plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom', size=14)
    # plt.yticks(np.arange(0.00, 2500, 250))
    # plt.tick_params(labelsize=16)
# =======
    # plt.plot(x_read_depth, CNNSSV_time,'o-',label='CNNSSV',color='r')
    # for label_x,label_y in zip(x_read_depth,CNNSSV_time):
    #     plt.text(label_x,label_y+0.05,'%.2f' %label_y, ha='center',va='bottom',size=10)
    # plt.plot(x_read_depth, nanomonsv_time,'o-',label='nanomonsv',color='g')
    # for label_x, label_y in zip(x_read_depth, nanomonsv_time):
    #     plt.text(label_x, label_y + 0.05, '%.2f' % label_y, ha='center', va='bottom', size=10)
    # plt.yticks(np.arange(0.00, 2500, 250))
    # # plt.tick_params(labelsize=)
    # plt.legend(loc='upper left',prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/simulate_time.png')
    # plt.close()


    #比较一下minimap2和ngmlr在0.2 0.5 0.7三种肿瘤纯度上的结果
    # plt.figure(figsize=(20,10))
    # name_list = ['ngmlr', 'minimap2']
    # CNNSSV_ngmlr_recall = [0.916,0.946,0.948]
    # CNNSSV_minimap2_recall = [0.758,0.804,0.824]
    # cutesv_ngmlr_recall = [0.91,0.942,0.94]
    # cutesv_minimap2_recall=[0.796,0.838,0.852]
    # sniffles_ngmlr_recall=[0.9,0.936,0.94]
    # sniffles_minimap2_recall=[0.766,0.804,0.796]
    # nanomonsv_ngmlr_recall=[0.24,0.298,0.34]
    # nanomonsv_minimap2_recall=[0.234,0.264,0.272]
    #
    #
    #
    #
    # x = list(range(2))
    # total_width, n = 0.8, 4
    # width = total_width / n
    #
    # plt.subplot(131)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.2", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_recall[0],CNNSSV_minimap2_recall[0]], width=width, label='CNNSSV', fc='r')
    # for label_x,label_y in zip(x,[CNNSSV_ngmlr_recall[0],CNNSSV_minimap2_recall[0]]):
    #     plt.text(label_x,label_y,'%.3f' %label_y, ha='center',va='bottom',size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x,[cutesv_ngmlr_recall[0],cutesv_minimap2_recall[0]], width=width, label='cutesv', fc='g',tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_recall[0],cutesv_minimap2_recall[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x,[sniffles_ngmlr_recall[0],sniffles_minimap2_recall[0]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_recall[0],sniffles_minimap2_recall[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_recall[0],nanomonsv_minimap2_recall[0]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_recall[0],nanomonsv_minimap2_recall[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.subplot(132)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.5", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_recall[1], CNNSSV_minimap2_recall[1]], width=width, label='CNNSSV', fc='r')
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_recall[1], CNNSSV_minimap2_recall[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_recall[1], cutesv_minimap2_recall[1]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_recall[1], cutesv_minimap2_recall[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_recall[1], sniffles_minimap2_recall[1]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_recall[1], sniffles_minimap2_recall[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_recall[1], nanomonsv_minimap2_recall[1]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_recall[1], nanomonsv_minimap2_recall[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    #
    # plt.subplot(133)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.7", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_recall[2], CNNSSV_minimap2_recall[2]], width=width, label='CNNSSV', fc='r')
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_recall[2], CNNSSV_minimap2_recall[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_recall[2], cutesv_minimap2_recall[2]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_recall[2], cutesv_minimap2_recall[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_recall[2], sniffles_minimap2_recall[2]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_recall[2], sniffles_minimap2_recall[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_recall[2], nanomonsv_minimap2_recall[2]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_recall[2], nanomonsv_minimap2_recall[2]]):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.legend(loc='lower right', bbox_to_anchor=(1.32, 0))
    # plt.savefig('/Users/duan/Desktop/minimap2_recall_vs.png')
    #
    #
    #
    # plt.figure(figsize=(20,10))
    # name_list = ['ngmlr', 'minimap2']
    # CNNSSV_ngmlr_precision = [0.997,0.993,0.991]
    # CNNSSV_minimap2_precision = [0.641,0.814,0.614]
    # cutesv_ngmlr_precision = [0.952,0.953,0.949]
    # cutesv_minimap2_precision=[0.567,0.550,0.547]
    # sniffles_ngmlr_precision=[0.834,0.812,0.800]
    # sniffles_minimap2_precision=[0.713,0.695,0.651]
    # nanomonsv_ngmlr_precision=[1.0,1.0,1.0]
    # nanomonsv_minimap2_precision=[0.975,0.985,0.993]
    #
    #
    #
    #
    # x = list(range(2))
    # total_width, n = 0.8, 4
    # width = total_width / n
    #
    # plt.subplot(131)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.2", fontsize=12)
    # plt.ylabel("Precision", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_precision[0],CNNSSV_minimap2_precision[0]], width=width, label='CNNSSV', fc='r')
    # for label_x,label_y in zip(x,[CNNSSV_ngmlr_precision[0],CNNSSV_minimap2_precision[0]]):
    #     plt.text(label_x,label_y,'%.3f' %label_y, ha='center',va='bottom',size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x,[cutesv_ngmlr_precision[0],cutesv_minimap2_precision[0]], width=width, label='cutesv', fc='g',tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_precision[0],cutesv_minimap2_precision[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x,[sniffles_ngmlr_precision[0],sniffles_minimap2_precision[0]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_precision[0],sniffles_minimap2_precision[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_precision[0],nanomonsv_minimap2_precision[0]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_precision[0],nanomonsv_minimap2_precision[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.subplot(132)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.5", fontsize=12)
    # plt.ylabel("Precision", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_precision[1], CNNSSV_minimap2_precision[1]], width=width, label='CNNSSV', fc='r')
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_precision[1], CNNSSV_minimap2_precision[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_precision[1], cutesv_minimap2_precision[1]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_precision[1], cutesv_minimap2_precision[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_precision[1], sniffles_minimap2_precision[1]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_precision[1], sniffles_minimap2_precision[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_precision[1], nanomonsv_minimap2_precision[1]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_precision[1], nanomonsv_minimap2_precision[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    #
    # plt.subplot(133)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.7", fontsize=12)
    # plt.ylabel("Precision", fontsize=12)
    # plt.bar(x, [CNNSSV_ngmlr_precision[2], CNNSSV_minimap2_precision[2]], width=width, label='CNNSSV', fc='r')
    #
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_precision[2], CNNSSV_minimap2_precision[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_precision[2], cutesv_minimap2_precision[2]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_precision[2], cutesv_minimap2_precision[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_precision[2], sniffles_minimap2_precision[2]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_precision[2], sniffles_minimap2_precision[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_precision[2], nanomonsv_minimap2_precision[2]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_precision[2], nanomonsv_minimap2_precision[2]]):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.legend(loc='lower right', bbox_to_anchor=(1.32, 0))
    # plt.savefig('/Users/duan/Desktop/minimap2_precision_vs.png')
    #



    # plt.figure(figsize=(20, 10))
    # name_list = ['ngmlr', 'minimap2']
    # CNNSSV_ngmlr_f1 = [0.955,0.969,0.969]
    # CNNSSV_minimap2_f1=[0.738,0.745,0.716]
    # # CNNSSV_minimap2_f1 = [0.694,0.696,0.704]
    # cutesv_ngmlr_f1 = [0.930,0.947,0.946]
    # cutesv_minimap2_f1 = [0.662,0.664,0.666]
    # sniffles_ngmlr_f1 = [0.866,0.869,0.864]
    # sniffles_minimap2_f1 = [0.694,0.696,0.704]
    # nanomonsv_ngmlr_f1 = [0.387,0.459,0.507]
    # nanomonsv_minimap2_f1 = [0.377,0.416,0.427]
    #
    # x = list(range(2))
    # total_width, n = 0.8, 4
    # width = total_width / n
    #
    # plt.subplot(131)
    # plt.tick_params(labelsize=16)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.2", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.bar(x, [CNNSSV_ngmlr_f1[0], CNNSSV_minimap2_f1[0]], width=width, label='CNNSSV', fc='r')
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_f1[0], CNNSSV_minimap2_f1[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_f1[0], cutesv_minimap2_f1[0]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_f1[0], cutesv_minimap2_f1[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_f1[0], sniffles_minimap2_f1[0]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_f1[0], sniffles_minimap2_f1[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_f1[0], nanomonsv_minimap2_f1[0]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_f1[0], nanomonsv_minimap2_f1[0]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.subplot(132)
    # plt.tick_params(labelsize=16)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.5", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.bar(x, [CNNSSV_ngmlr_f1[1], CNNSSV_minimap2_f1[1]], width=width, label='CNNSSV', fc='r')
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_f1[1], CNNSSV_minimap2_f1[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_f1[1], cutesv_minimap2_f1[1]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_f1[1], cutesv_minimap2_f1[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_f1[1], sniffles_minimap2_f1[1]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_f1[1], sniffles_minimap2_f1[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_f1[1], nanomonsv_minimap2_f1[1]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_f1[1], nanomonsv_minimap2_f1[1]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    #
    # plt.subplot(133)
    # plt.tick_params(labelsize=16)
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # plt.ylim(0, 1)
    # plt.xlabel("Purity=0.7", fontsize=18)
    # plt.ylabel("F1-score", fontsize=18)
    # plt.bar(x, [CNNSSV_ngmlr_f1[2], CNNSSV_minimap2_f1[2]], width=width, label='CNNSSV', fc='r')
    #
    # for label_x, label_y in zip(x, [CNNSSV_ngmlr_f1[2], CNNSSV_minimap2_f1[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [cutesv_ngmlr_f1[2], cutesv_minimap2_f1[2]], width=width, label='cutesv', fc='g',
    #         tick_label=name_list)
    # for label_x, label_y in zip(x, [cutesv_ngmlr_f1[2], cutesv_minimap2_f1[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # # plt.bar(x, sniffles_f1, width=width, label='sniffles', tick_label=name_list, fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [sniffles_ngmlr_f1[2], sniffles_minimap2_f1[2]], width=width, label='sniffles', fc='b')
    # for label_x, label_y in zip(x, [sniffles_ngmlr_f1[2], sniffles_minimap2_f1[2]]):
    #     plt.text(label_x, label_y, '%.3f' % label_y, ha='center', va='bottom', size=12)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, [nanomonsv_ngmlr_f1[2], nanomonsv_minimap2_f1[2]], width=width, label='nanomonsv', fc='y')
    # for label_x, label_y in zip(x, [nanomonsv_ngmlr_f1[2], nanomonsv_minimap2_f1[2]]):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom', size=12)
    # plt.legend(loc='lower right', bbox_to_anchor=(1.45, 0),prop={'size': 14})
    # plt.savefig('/Users/duan/Desktop/minimap2_f1_vs.png')



#分析k

    #先画一下 somatic_unique_k-mer对于四种变异，在somatic和germline sv附近的数量
    # DEL_somatic=0.9055755395683454
    # INS_somatic=0.9580592105263158
    # INV_somatic=0.8978674892703863
    # DUP_somatic=0.9075
    #


    # somatic=[0.9347876537479693,0.9889643463497454,0.9268309566662051,0.9367741935483872]
    # germline=[0.06362951807228916,0.06122568893589517,0.07674002359354025,0.0583908300264093]
    #
    # plt.figure(figsize=(20,10))
    # name_list = ['DEL','INS','INV','DUP']
    # ax = plt.gca()  # gca:get current axis得到当前轴
    # # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    #
    #
    # x = list(range(len(somatic)))
    # total_width, n = 0.8, 3
    # width = total_width / n
    # plt.ylim(0, 1)
    # plt.xlabel("SV type", fontsize=18)
    # plt.ylabel("tumor unique k-mer radio", fontsize=18)
    # plt.tick_params(labelsize=16)
    # plt.bar(x, somatic, width=width, label='somatic sv', fc='r')
    # for label_x,label_y in zip(x,somatic):
    #     plt.text(label_x,label_y,'%.2f' %label_y, ha='center',va='bottom',size=15)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, germline, width=width, label='germline sv',fc='g')
    # for label_x, label_y in zip(x, germline):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom',size=15)
    #
    #
    #
    # plt.xticks([index + width/2 for index in range(len(name_list))], name_list)
    # # plt.legend(loc='lower left',prop={'size': 16},bbox_to_anchor=(1.45, 0))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.13, 0),prop={'size': 14})
    # # plt.legend()
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/tumor_unique_k-mer.png')
    #
    #
    #
    # somatic = [0.9409976295990929, 0.9111710356993101, 0.9036470364431882, 0.0696450878095378]
    # germline = [0.05632072812210544, 0.050946663153536347, 0.03771204533985482, 0.0473739909272177]
    #
    #
    # plt.figure(figsize=(20, 10))
    # name_list = ['DEL', 'INS', 'INV', 'DUP']
    #
    # ax = plt.gca()  # gca:get current axis得到当前轴
    #     # 设置图片的右边框和上边框为不显示
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # x = list(range(len(somatic)))
    # total_width, n = 0.8, 3
    # width = total_width / n
    # plt.ylim(0, 1)
    # plt.xlabel("SV type", fontsize=18)
    # plt.ylabel("tumor lost k-mer radio", fontsize=18)
    # plt.tick_params(labelsize=16)
    # plt.bar(x, somatic, width=width, label='somatic sv', fc='r')
    # for label_x, label_y in zip(x, somatic):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom', size=15)
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, germline, width=width, label='germline sv', fc='g')
    # for label_x, label_y in zip(x, germline):
    #     plt.text(label_x, label_y, '%.2f' % label_y, ha='center', va='bottom', size=15)
    #
    # plt.xticks([index + width / 2 for index in range(len(name_list))], name_list)
    # # plt.legend(loc='lower left',prop={'size': 16},bbox_to_anchor=(1.45, 0))
    # plt.legend(loc='lower right', bbox_to_anchor=(1.13, 0), prop={'size': 14})
    # # plt.legend()
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/tumor_lost_k-mer_radio.png')
