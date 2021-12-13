import os
if __name__ == '__main__':
    # command = "python main.py --tumor '/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/mixed.chr20.bam' --normal '/home/duan/Desktop/somaticSV/bam/NA19239_NA19240_mixed/0.7/NA19239.chr20.bam' --ref '/home/duan/Data/ref/chr20.fa'  --wkdir ~/Desktop/test -t 1"
    command="python main.py --tumor '/home/duan/Desktop/somaticSV/bam/NA19238_NA19239_mixed/0.7.mixed.chr20.bam' --normal '/home/duan/Desktop/somaticSV/bam/NA19238_NA19239_mixed/NA19238.chr20.bam' --ref '/home/duan/Data/ref/chr20.fa' --model '/home/duan/Desktop/getBreakpoint/model/CNN_sup_12_1.model' --wkdir '/home/duan/Desktop/test' --output ~/Desktop/output.bed -t 1"
    os.system(command)


