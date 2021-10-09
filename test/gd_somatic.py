if __name__ == '__main__':

    normal_gd=open('/Users/duan/Desktop/results/somaticSV/random_SV/gd/chr20_sim_germline_dup.bed','r')
    tumor_gd=open('/Users/duan/Desktop/results/somaticSV/random_SV/gd/chr20_sim_somatic_dup.bed','r')


    somatic_gd=open('/Users/duan/Desktop/results/somaticSV/random_SV/gd/gd_chr20_sim_somatic_dup.bed','w')



    normal_lines=list()
    tumor_lines=list()
    while True:
        l=normal_gd.readline()
        if l:
            normal_lines.append(l)
        else:
            break
    while True:
        l=tumor_gd.readline()
        if l:
            tumor_lines.append(l)
        else:
            break

    for i in tumor_lines:
        if i not in normal_lines:
            somatic_gd.write(i)

    somatic_gd.close()
    normal_gd.close()
    tumor_gd.close()
