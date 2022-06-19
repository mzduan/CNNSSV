# CNNSSV
基于卷积神经网络的体细胞结构变异检测算法

## 简介
本算法一共包括三个部分，分别为检测潜在体细胞结构变异、编码与字符串特征提取、基于神经网络的分类。第一部分以肿瘤样本测序文件tumor.bam作为输入，找出包含变异信号的reads，并对其进行聚类，得到tumor.bam中所有的结构变异；第二部分是本算法的核心模块，以肿瘤样本测序文件tumor.bam、正常样本测序文件normal.bam、参考基因组reference.fa作为输入，对于第一部分检测出的潜在结构变异，将比对信息编码成两张RGB三通道 的图片，肿瘤样本和正常样本各一张，并提取结构变异断点附近的字符串特征，得到 维的特征向量；第三部分以卷积层为核心结构搭建神经网络，神经网络接收图片和特征向量这两个输入，给出分类结果，若结果为真，则为体细胞结构变异

## 使用方法
    python main.py --tumor "tumor bam" --normal "normal bam" --ref reference fasta" --model "trained cnn model" 
    --wkdir "work dir" --output "output sv bed" -t", help="thead number"
    
## 模型训练
   1. 运行/scripts/simulate_fa.sh 和/scripts/simulate_CCS.pbs 得到测序数据，并运行本算法python gen_features.py提取特征，再运行/scripts/tagging.sh脚本将计算得到的特征进行分类，得到标注好的训练数据
   2. 运行train.py进行模型训练
  
## 评估实验结果
    1.cutesv和sniffles的结果需要取差得到，请运行/scripts/get_somatic_vcf_cutesv.py和/scripts/get_somatic_vcf_sniffles.py
    2.运行/scripts/vcf2bed.py将vcf格式转换为bed格式
    3.运行/scripts/evaluate.py评估各方法在模拟数据上的性能，运行/scripts/cmp_NA19240.py评估各方法在NA19238-N19239混合数据上的性能
    
