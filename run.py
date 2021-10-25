import os
if __name__ == '__main__':
    command="python main.py --tumor '/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/mixed.chr20.bam' --normal '/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/NA19239.chr20.bam' --ref '/home/duan/Data/ref/chr20.fa' --model '/home/duan/Desktop/somaticSV/cnn_10_24.model' --wkdir ~/Desktop/test --output ~/Desktop/output.bed -t 1"
    os.system(command)


