import os
if __name__ == '__main__':
    ccs_feat_path='/home/mzduan/somaticSV/CCS/tag'
    for p in ["bam_0.2", "bam_0.5", "bam_0.7"]:
        for c in range(1, 23, 1):
            if c == 20:
                continue
            current_feat_path = ccs_feat_path + '/' + p + '/chr' + str(c)
            germline_path = current_feat_path + '/germline'
            for f in os.listdir(germline_path):
                if f[0] != '.':
                    absolute_path = germline_path + '/' + f
                    n_flag=False
                    t_flag=False
                    s_flag=False
                    for image in os.listdir(absolute_path):
                        if image[0] == 'n':
                            n_flag=True
                        elif image[0] == 't':
                            t_flag = True
                        elif image[0] == 's':
                            s_flag=True
                    if n_flag==False or t_flag==False:
                        print(absolute_path)
            somatic_path = current_feat_path + '/somatic'
            for f in os.listdir(somatic_path):
                if f[0] != '.':
                    absolute_path = somatic_path + '/' + f
                    n_flag=False
                    t_flag=False
                    s_flag=False
                    for image in os.listdir(absolute_path):
                        if image[0] == 'n':
                            n_flag=True
                        elif image[0] == 't':
                            t_flag = True
                        elif image[0] == 's':
                            s_flag=True
                    if n_flag==False or t_flag==False:
                        print(absolute_path)