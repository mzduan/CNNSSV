import re
import os
if __name__ == '__main__':

    typedict={'insertion':'INS','deletion':'DEL','tandem duplication':'DUP','inversion':'INV'}

    svdict=dict()


    tagged_dir = '/home/mzduan/somaticSV/tag/'




    #首先读取somatic sv的groundtruth
    for i in range(1,23):
        bed_file='/home/mzduan/somaticSV/sv/chr'+str(i)+'.somatic.bed'
        svdict[str(i)]=list()
        with open(bed_file,'r') as fin:
            while True:
                l=fin.readline()
                if l:
                    arrays=re.split('\s+',l)
                    start=int(arrays[1])
                    end=int(arrays[2])
                    sv_type=arrays[3]
                    sv_type=typedict[sv_type]
                    svdict[str(i)].append([sv_type,start,end])
                else:
                    break
    for suffix in ['bam_0.2/','bam_0.5/','bam_0.7/']:
        bam_prefix='/home/mzduan/somaticSV/features/'+suffix

        os.system('mkdir '+tagged_dir+suffix)


        for i in range(1,23):
            chr_dir=bam_prefix+'chr'+str(i)
            tagged_germline_dir=tagged_dir+suffix+'chr'+str(i)+'/germline'
            tagged_somatic_dir=tagged_dir+suffix+'chr'+str(i)+'/somatic'
            os.system('mkdir '+tagged_dir+suffix+'chr'+str(i))
            os.system('mkdir '+tagged_germline_dir)
            os.system('mkdir '+tagged_somatic_dir)
            for f in os.listdir(chr_dir):
                splits=re.split('_',f)
                if len(splits)==3:

                    absolute_path = chr_dir + '/'+f
                    sv_type=splits[0]
                    sv_start=int(splits[1])
                    sv_end=sv_start+int(splits[2])

                    find_flag=False
                    if sv_type=='INS':
                        sv_end=sv_start+1
                    for gd in svdict[str(i)]:
                        if sv_type==gd[0] and abs(sv_start-gd[1])<=50 and abs(sv_end-gd[2])<=50:
                            os.system('scp -r '+absolute_path+' '+tagged_somatic_dir)
                            find_flag=True
                            break
                    if not find_flag:
                        os.system('scp -r ' + absolute_path + ' ' + tagged_germline_dir)


