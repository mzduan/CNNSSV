import re
if __name__ == '__main__':

    #过滤得到somatic sv ,somatic.vcf和germline.vcf求差
    germline_vcf='/Users/duan/Desktop/results/various_depth/0.7/20/sniffles.normal.vcf'
    somatic_vcf='/Users/duan/Desktop/results/various_depth/0.7/sniffles.tumor.vcf'
    output='/Users/duan/Desktop/results/various_depth/0.7/20/sniffles.somatic.bed'
    caller='sniffles'


    forward_bk1=0
    forward_bk2=0
    forward_svtype=""
    #
    germline_callset = list()
    with open(germline_vcf,'r') as fin:
        while True:
            l=fin.readline()
            if l:
                if l[0]=='c':
                    l=re.split('\s+',l)
                    chr=l[0]
                    start=l[1]
                    extern_flag=l[7]
                    if caller=='sniffles':
                        sv_type_info=extern_flag.split(';')[8]
                        sv_type=sv_type_info.split('=')[1]
                        end_info=extern_flag.split(';')[3]
                        end=end_info.split('=')[1]
                        if sv_type!='BND':
                            germline_callset.append([chr, int(start), int(end), sv_type])
                    elif caller=='cutesv':
                        sv_type_info = extern_flag.split(';')[1]
                        sv_type = sv_type_info.split('=')[1]
                        end_info = extern_flag.split(';')[3]
                        end = end_info.split('=')[1]
                        if abs(forward_bk1 - int(start)) <= 20 and abs(forward_bk2 - int(end)) <= 20 and sv_type==forward_svtype=='INV':
                            forward_bk1 = int(start)
                            forward_bk2 = int(end)
                            forward_svtype=sv_type
                        else:
                            if sv_type != 'BND':
                                germline_callset.append([chr, int(start), int(end), sv_type])
                            forward_bk1 = int(start)
                            forward_bk2 = int(end)
                            forward_svtype=sv_type
            else:
                break


    # 处理bed文件
    # 用于处理自定义的bed文件
    # with open(germline_vcf,'r') as fin:
    #     while True:
    #         l=fin.readline()
    #         if l:
    #             splits=re.split('\s+',l)
    #             chrom=splits[0]
    #             start=splits[1]
    #             end=splits[2]
    #             sv_type=splits[3]
    #             germline_callset.append([chrom,int(start),int(end),sv_type])
    #         else:
    #             break

    forward_bk1=0
    forward_bk2=0
    forward_svtype=""


    somatic_callset=list()
    with open(somatic_vcf,'r') as fin:
        while True:
            l=fin.readline()
            if l:
                if l[0]=='c':
                    l=re.split('\s+',l)
                    chr=l[0]
                    start=l[1]
                    extern_flag=l[7]
                    if caller=='sniffles':
                        sv_type_info=extern_flag.split(';')[8]
                        sv_type=sv_type_info.split('=')[1]
                        end_info=extern_flag.split(';')[3]
                        end=end_info.split('=')[1]
                        if sv_type!='BND':
                            somatic_callset.append([chr, int(start), int(end), sv_type])
                    elif caller=='cutesv':
                        sv_type_info = extern_flag.split(';')[1]
                        sv_type = sv_type_info.split('=')[1]
                        end_info = extern_flag.split(';')[3]
                        end = end_info.split('=')[1]
                        if abs(forward_bk1 - int(start)) <= 20 and abs(forward_bk2 - int(end)) <= 20 and sv_type==forward_svtype=='INV':
                            forward_bk1 = int(start)
                            forward_bk2 = int(end)
                            forward_svtype=sv_type
                        else:
                            if sv_type != 'BND':
                                somatic_callset.append([chr, int(start), int(end), sv_type])
                            forward_bk1 = int(start)
                            forward_bk2 = int(end)
                            forward_svtype=sv_type
            else:
                break

    # with open(somatic_vcf,'r') as fin:
    #     while True:
    #         l=fin.readline()
    #         if l:
    #             splits=re.split('\s+',l)
    #             chrom = splits[0]
    #             start=splits[1]
    #             end=splits[2]
    #             sv_type=splits[3]
    #             somatic_callset.append([chrom,int(start),int(end),sv_type])
    #         else:
    #             break



    difference=list()
    for i in somatic_callset:
        somatic_start=i[1]
        somatic_end=i[2]
        somatic_type=i[3]
        find_flag=False
        for j in germline_callset:
            germline_start=j[1]
            germline_end=j[2]
            germline_type=i[3]

            if somatic_type==germline_type and abs(somatic_start-germline_start)<=20 and abs(somatic_end-germline_end)<=20:
                find_flag=True
        if not find_flag:
            difference.append(i)


    with open(output,'w') as fout:
        for sv in difference:
            fout.write(sv[0]+'\t'+str(sv[1])+'\t'+str(sv[2])+'\t'+sv[3]+'\n')
