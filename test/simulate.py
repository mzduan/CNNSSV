import random
if __name__ == '__main__':
    # chr20_del=open('/Users/duan/Desktop/chr20_sim_dup.bed','w')
    # with open('/Users/duan/Downloads/生信工具/cuteSV-master/simulation/sim_dup.bed','r') as fin:
    #     while True:
    #         l=fin.readline()
    #         if l:
    #             infos=re.split('\s+',l)
    #             if infos[0]=='20':
    #                 chr20_del.write('chr'+l)
    #         else:
    #             break
    # chr20_del.close()


    lines=list()
    with open('/Users/duan/Desktop/chr20_sim_somatic_dup.bed', 'r') as fin:
        while True:
            l=fin.readline()
            if l:
                lines.append(l)
            else:
                break

    counts=len(lines)
    print(counts)
    germline_counts=int(counts*0.8)
    print(germline_counts)

    random_lines=random.sample(range(0, counts), germline_counts)


    fout=open('/Users/duan/Desktop/chr20_sim_germline_dup.bed', 'w')
    for i in random_lines:
        fout.write(lines[i])
    fout.close()




