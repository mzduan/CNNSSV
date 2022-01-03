import matplotlib.pyplot as plt
import numpy as np
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
    # plt.figure(figsize=(18,8))
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
    # # plt.title(')
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    #
    # plt.xticks(np.arange(0.2,0.8,0.1))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/recall.png')
    # #
    # # plt.close()
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Precsion", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/precision.png')
    # # plt.close()
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.show()
    # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/simulate.png')
    # #
    # plt.close()




    #杂合模拟数据
    # plt.figure(figsize=(18,8))
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
    # # plt.title(')
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    #
    # plt.xticks(np.arange(0.2,0.8,0.1))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/recall.png')
    #
    # # plt.close()
    #
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Precsion", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/precision.png')
    # # plt.close()
    #
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.show()
    # # plt.legend(loc='lower right')
    # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/heter_simulate.png')
    # #
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
    # # plt.legend(loc=2, bbox_to_anchor=(1.05, 1))
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
    # # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    #
    #
    #
    #
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
    # # plt.legend(loc=2,bbox_to_anchor=(1.05,1))
    # # plt.legend(loc='lower center')
    # plt.legend(loc='lower right', bbox_to_anchor=(1.32, 0))
    #
    #
    # # plt.show()
    # plt.savefig('/Users/duan/Desktop/random.png')




    # #纯合模拟数据 normal样本测序深度发生变化时的结果，purity=0.2
    # # plt.figure(figsize=(18,8))
    # x_read_depth = [5,10,15,20,25]
    # #
    # CNNSSV_precision = [0.991,0.997,0.995,0.997,0.997]
    # cutesv_precision = [0.953,0.955,0.955,0.952,0.953]
    # sniffles_precision = [0.803,0.816,0.830,0.834,0.825]
    # nanomonsv_precision = [0.983,0.991,0.991,1.0,0.991]
    # #
    # # CNNSSV_f1=[]
    # # cutesv_f1=[]
    # # sniffles_f1=[]
    # # nanomonsv_f1=[]
    # #
    # # # plt.title(')
    # # plt.subplot(131)
    # # plt.ylim(0.5,1)
    # # plt.xlabel("Purity", fontsize=12)
    # # plt.ylabel("Recall", fontsize=12)
    # # plt.grid()
    # # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    # #
    # # plt.xticks(np.arange(0.2,0.8,0.1))
    # # plt.yticks(np.arange(0.00,1.01,0.25))
    # # # plt.legend(loc='lower right')
    # # # plt.savefig('/Users/duan/Desktop/recall.png')
    # # #
    # # # plt.close()
    # # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read_depth", fontsize=12)
    # plt.ylabel("Precsion", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(5, 25.1, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/precision.png')
    # # # plt.close()
    # # plt.subplot(133)
    # # plt.ylim(0.5, 1)
    # # plt.xlabel("Purity", fontsize=12)
    # # plt.ylabel("F1-score", fontsize=12)
    # # plt.grid()
    # # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    # #
    # # plt.xticks(np.arange(0.2, 0.8, 0.1))
    # # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # # plt.show()
    # # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/simulate.png')
    # # #
    # plt.close()




    #纯合模拟数据 tumor样本测序深度发生变化时的结果，purity=0.2
    # plt.figure(figsize=(18,8))
    # x_read_depth = [10,15,20,25,30,35]
    # #
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
    # #
    # CNNSSV_f1=[0.897,0.930,0.955,0.962,0.963,0.964]
    # cutesv_f1=[0.865,0.914,0.930,0.937,0.945,0.944]
    # sniffles_f1=[0.842,0.864,0.866,0.883,0.864,0.878]
    # nanomonsv_f1=[0.239,0.341,0.387,0.417,0.439,0.442]
    # #
    # # plt.title(')
    # plt.subplot(131)
    # plt.ylim(0.5,1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("Recall", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_recall,'o-',label='CNNSSV',color='r',)
    # plt.plot(x_read_depth, cutesv_recall,'o-',label='cutesv',color='g')
    # plt.plot(x_read_depth, sniffles_recall,'o-',label='sniffles',color='b')
    # plt.plot(x_read_depth, nanomonsv_recall,'o-',label='nanomonsv',color='y')
    #
    # plt.xticks(np.arange(10,36,5))
    # plt.yticks(np.arange(0.00,1.01,0.25))
    # # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/recall.png')
    # #
    # # plt.close()
    # plt.subplot(132)
    # plt.ylim(0.5, 1)
    # plt.xlabel("read_depth", fontsize=12)
    # plt.ylabel("Precsion", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_precision, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_precision, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_precision, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_precision, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # plt.legend(loc='lower right')
    # # plt.savefig('/Users/duan/Desktop/precision.png')
    # # # plt.close()
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.show()
    # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/tumor_vary_depth.png')
    # # #
    # plt.close()


    #杂合模拟数据，normal样本测序深度发生变化时precision的和F1的变化
    plt.figure(figsize=(15,8))
    x_read_depth = [5,10,15,20,25]
    #
    # CNNSSV_recall = [0.816,0.874,0.916,0.932,0.934,0.936]
    # cutesv_recall = [0.8,0.87,0.91,0.918,0.932,0.94]
    # sniffles_recall = [0.798,0.856,0.9,0.92,0.922,0.936]
    # nanomonsv_recall = [0.136,0.206,0.24,0.264,0.282,0.284]

    CNNSSV_precision = [0.885,0.987,0.994,0.994,0.994]
    cutesv_precision = [0.845,0.946,0.957,0.959,0.954]
    sniffles_precision = [0.756,0.832,0.850,0.860,0.852]
    nanomonsv_precision = [0.752,.972,1.0,1.0,1.0]

    #
    CNNSSV_f1=[0.835,0.881,0.883,0.881,0.880]
    cutesv_f1=[0.811,0.855,0.859,0.860,0.858]
    sniffles_f1=[0.766,0.803,0.811,0.815,0.812]
    nanomonsv_f1=[0.236,0.244,0.248,0.248,0.239]
    #
    # plt.title(')
    plt.subplot(121)
    plt.ylim(0.5,1)
    plt.xlabel("Purity", fontsize=12)
    plt.ylabel("Precision", fontsize=12)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_precision,'o-',label='CNNSSV',color='r',)
    plt.plot(x_read_depth, cutesv_precision,'o-',label='cutesv',color='g')
    plt.plot(x_read_depth, sniffles_precision,'o-',label='sniffles',color='b')
    plt.plot(x_read_depth, nanomonsv_precision,'o-',label='nanomonsv',color='y')

    plt.xticks(np.arange(2,26,5))
    plt.yticks(np.arange(0.00,1.01,0.25))
    # plt.legend(loc='lower right')
    # plt.savefig('/Users/duan/Desktop/recall.png')
    #
    # plt.close()
    plt.subplot(122)
    plt.ylim(0.5, 1)
    plt.xlabel("read_depth", fontsize=12)
    plt.ylabel("F1-score", fontsize=12)
    plt.grid()
    plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')

    plt.xticks(np.arange(5, 26, 5))
    plt.yticks(np.arange(0.00, 1.01, 0.25))
    plt.legend(loc='lower right', bbox_to_anchor=(1.28, 0))
    plt.savefig('/Users/duan/Desktop/precision.png')
    # plt.close()
    # plt.subplot(133)
    # plt.ylim(0.5, 1)
    # plt.xlabel("Purity", fontsize=12)
    # plt.ylabel("F1-score", fontsize=12)
    # plt.grid()
    # plt.plot(x_read_depth, CNNSSV_f1, 'o-', label='CNNSSV', color='r', )
    # plt.plot(x_read_depth, cutesv_f1, 'o-', label='cutesv', color='g')
    # plt.plot(x_read_depth, sniffles_f1, 'o-', label='sniffles', color='b')
    # plt.plot(x_read_depth, nanomonsv_f1, 'o-', label='nanomonsv', color='y')
    #
    # plt.xticks(np.arange(10, 36, 5))
    # plt.yticks(np.arange(0.00, 1.01, 0.25))
    # # plt.show()
    # plt.legend(loc='lower right', bbox_to_anchor=(1.35, 0))
    # plt.savefig('/Users/duan/Desktop/tumor_vary_depth.png')
    # # #
    # plt.close()





