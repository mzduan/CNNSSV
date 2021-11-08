import os
if __name__ == '__main__':
    # command = "python main.py --tumor '/home/duan/Desktop/somaticSV/bam/CCS/0.7/somatic_bam_chr20/sim.srt.bam' --normal '/home/duan/Desktop/somaticSV/bam/CCS/0.7/germline_bam_chr20/sim.srt.bam' --ref '/home/duan/Data/ref/chr20.fa'  --wkdir ~/Desktop/test -t 4"
    command="python main.py --tumor '/home/duan/Desktop/somaticSV/bam/CCS/0.5/somatic_bam_chr20/sim.srt.bam' --normal '/home/duan/Desktop/somaticSV/bam/CCS/0.7/germline_bam_chr20/sim.srt.bam' --ref '/home/duan/Data/ref/chr20.fa' --model '/home/duan/Desktop/somaticSV/Siamese_v1.model' --wkdir '/home/duan/Desktop/test' --output ~/Desktop/output.bed -t 4"
    os.system(command)


