import re
if __name__ == '__main__':
    somatic_vcf=open('/home/duan/Desktop/getBreakpoint/groundtruth/NA19239_NA19240/NA19239.chr20.somatic.vcf','r')
    filter_vcf=open('/home/duan/Desktop/getBreakpoint/groundtruth/NA19239_NA19240/NA19239.chr20.somatic.filtered.vcf','w')

    while True:
        l=somatic_vcf.readline()
        if l:
            if 'IMPRECISE' not in l:
                filter_vcf.write(l)
        else:
            break
    somatic_vcf.close()
    filter_vcf.close()