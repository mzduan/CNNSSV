import pysam
from PIL import Image
import numpy as np
if __name__ == '__main__':
    # normal=Image.open('/home/mzduan/somaticSV/CCS/tag_with_confusion/bam_0.7/chr22/germline/chr22_DUP_31943985_492_42/tumor.png')
    sup_feat = np.load('/home/mzduan/somaticSV/CCS/tag_with_confusion/bam_0.7/chr22/germline/chr22_DUP_36384861_509_50/sup_feat.npy')
    print(sup_feat)