import re
if __name__ == '__main__':
    NA19240=open('/Users/duan/Desktop/results/somaticSV/callset/gd/nstd152.GRCh38.variant_call.NA19240.bed','r')

    forward_start=-1
    forward_end=-1
    forward_chr=1
    min_sv_distance=100000000

    while True:
        l=NA19240.readline()
        if l:
            infos=re.split('\s+',l)
            chrom=infos[0]
            sv_start=int(infos[1])
            sups=infos[7]

            experiment_pos = sups.find(';EXPERIMENT')
            experiment_pair = ""
            for k in range(experiment_pos + 1, len(sups)):
                if sups[k] != ';':
                    experiment_pair = experiment_pair + sups[k]
                else:
                    break
            experiment_id = int(experiment_pair.split('=')[1])
            if int(experiment_id)!=5:
                # print(int(experiment_id))
                continue



            end_pos = sups.find(';END')
            end_pair = ""
            for k in range(end_pos + 1, len(sups)):
                if sups[k] != ';':
                    end_pair = end_pair + sups[k]
                else:
                    break
            sv_end = int(end_pair.split('=')[1])




            if chrom==forward_chr:

                if sv_start<=forward_end:
                    continue
                if sv_start-forward_end==11:
                    print(sv_start,forward_end)

                min_sv_distance=min(min_sv_distance,sv_start-forward_end)
                forward_start=sv_start
                forward_end=sv_end
            else:
                forward_chr=chrom
                forward_start=sv_start
                forward_end=sv_end
        else:
            break

    print(min_sv_distance)
    NA19240.close()