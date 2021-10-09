import pysam
import re
import reference
import bisect
import SimpleAln
import sys
# from breakpoints import get_reverse_seq
base_dict={'A':'1','C':'2','G':'4','T':'8','N':'9'}


def get_reverse_seq(seq):
    reverse_seq=""
    for i in range(len(seq)-1,-1,-1):
        if seq[i]=='A':
            reverse_seq=reverse_seq+'T'
        elif seq[i]=='T':
            reverse_seq=reverse_seq+'A'
        elif seq[i]=='C':
            reverse_seq=reverse_seq+'G'
        elif seq[i]=='G':
            reverse_seq=reverse_seq+'C'
        elif seq[i]=='N':
            reverse_seq=reverse_seq+'N'
    return reverse_seq

def transform(seq):
    transformed=""
    for i in range(len(seq)):
        transformed=transformed+base_dict[seq[i]]
    return transformed

def get_pos(revised_pos,p):
    list_keys=list(revised_pos.keys())
    index = bisect.bisect_right(list_keys, p)
    deviation=0
    for i in range(index):
        deviation=deviation+ revised_pos[list_keys[i]]

    return p+deviation

def update(seq,update_list):
    sorted_update_list=sorted(update_list,key=lambda item:item[0],reverse=True)

    #检查坐标是否有overlap
    # for i in range(len(sorted_update_list)-1):
        # if sorted_update_list[i][0]<sorted_update_list[i+1][1]:
        #     print(sorted_update_list)



    list_seq=list(seq)
    for i in sorted_update_list:
        list_seq[i[0]:i[1]]=i[2]

    updated_seq="".join(list_seq)
    return updated_seq

def correct_S(seq,aln,join_SA,ref_seq,revised_dict):
    read_name=aln.query_name
    if read_name not in join_SA.keys():
        raise Exception("Error read name")
    read_alns=join_SA[read_name]
    if len(read_alns)==1:  #没有SA，无法矫正
        return seq
    else:

        #确定primary的方向
        for a in read_alns:
            if a.is_pri==True:
                pri_direction=a.direction


        update_revised_seq=list()
        for a in read_alns:
            if a.is_pri==False:

                #确定 SA 比对的是primary query seq中的哪一部分

                revised_S_start = 0
                if a.cigar[0][0] == 4 or a.cigar[0][0] ==5 :
                    revised_S_start = a.cigar[0][1]

                revised_S_end = 0
                for c in a.cigar:
                    if c[0] == 4 or c[0]==5 :
                        revised_S_end = revised_S_end + c[1]
                    elif c[0] == 0 or c[0] == 1:
                        revised_S_end = revised_S_end + c[1]

                if a.cigar[-1][0] == 5 or a.cigar[-1][0] == 4:
                    revised_S_end = revised_S_end - a.cigar[-1][-1]

                if a.direction==pri_direction:
                    start_pos_in_revised=get_pos(revised_dict,revised_S_start)
                    end_pos_in_revised=get_pos(revised_dict,revised_S_end)

                    # print(seq[start_pos_in_revised:end_pos_in_revised])
                    revised_subseq=""
                    read_pos=0
                    ref_pos=a.ref_start
                    for c in a.cigar:
                        if c[0]==0:
                            revised_subseq=revised_subseq+ref_seq[ref_pos:ref_pos+c[1]]
                            read_pos=read_pos+c[1]
                            ref_pos=ref_pos+c[1]
                        elif c[0]==1:
                            if c[1]>=50:
                                revised_subseq=revised_subseq+aln.query_sequence[read_pos:read_pos+c[1]]
                            read_pos=read_pos+c[1]
                        elif c[0]==2:
                            if c[1]<50:
                                revised_subseq=revised_subseq+ref_seq[ref_pos:ref_pos+c[1]]
                            ref_pos=ref_pos+c[1]
                        elif c[0]==4:
                            read_pos=read_pos+c[1]
                    update_revised_seq.append( (start_pos_in_revised,end_pos_in_revised,revised_subseq))
                else:

                    query_sequence = get_reverse_seq(aln.query_sequence)
                    temp=revised_S_start
                    revised_S_start=aln.query_length-revised_S_end
                    revised_S_end=aln.query_length-temp

                    start_pos_in_revised=get_pos(revised_dict,revised_S_start)
                    end_pos_in_revised=get_pos(revised_dict,revised_S_end)

                    revised_subseq=""
                    read_pos=0
                    ref_pos=a.ref_start
                    for c in a.cigar:
                        if c[0]==0:
                            revised_subseq=revised_subseq+ref_seq[ref_pos:ref_pos+c[1]]
                            read_pos=read_pos+c[1]
                            ref_pos=ref_pos+c[1]
                        elif c[0]==1:
                            if c[1]>=50:
                                revised_subseq=revised_subseq+query_sequence[read_pos:read_pos+c[1]]
                            read_pos=read_pos+c[1]
                        elif c[0]==2:
                            if c[1]<50:
                                revised_subseq=revised_subseq+ref_seq[ref_pos:ref_pos+c[1]]
                            ref_pos=ref_pos+c[1]
                        elif c[0]==5:
                            read_pos=read_pos+c[1]


                    update_revised_seq.append((start_pos_in_revised, end_pos_in_revised, get_reverse_seq(revised_subseq)))

        updated=update(seq,update_revised_seq)
        # print(updated)
        return updated


def getSA(bam_file_name):
    bam = pysam.AlignmentFile(bam_file_name, 'r')
    aligments=dict()
    for aln in bam:
        if not aln.is_unmapped and not aln.is_secondary:
            if aln.has_tag('SA'):
                simpled = SimpleAln.SimpleAln(aln.reference_start,aln.is_reverse, aln.cigartuples, aln.is_supplementary)
                if aln.query_name in aligments.keys():
                    aligments[aln.query_name].append(simpled)
                else:
                    aligments[aln.query_name]=[simpled]
    bam.close()
    return aligments






def correct_byRef(bam_file_name,ref_file,output_dir,flag):

    k_size=31
    min_sv_size=50
    corrected_output=output_dir+'/'+flag+'_corrected.txt'
    corrected_name=output_dir+'/'+flag+'_name.txt'
    fout=open(corrected_output,'w')
    fname=open(corrected_name,'w')
    ref_dict = reference.initial_fa(ref_file)
    bam=pysam.AlignmentFile(bam_file_name,'r')

    # print("Extract all supplement aligments by read_name")
    join_SA=getSA(bam_file_name)

    # print("Start correction")
    # counts = 1
    for aln in bam:

        if aln.query_name=="C2_H1_27655":
            # if counts%10000==0:
            #     print(str(counts)+"\talignments have been corrected")
            # counts=counts+1

            if aln.is_secondary: continue
            if aln.is_supplementary: continue

            if aln.is_unmapped or aln.mapping_quality<20:
                continue
            elif aln.query_length < k_size+3:
                continue

            quality = aln.query_qualities
            lowq_num = 0
            for i in range(len(quality)):
                if quality[i]+33<=ord('#'):
                    lowq_num=lowq_num+1

            if float(lowq_num)/len(quality) >= 0.5:
                continue
            else:
                corrected_seq=""
                current_read_pos=0
                current_ref_pos=aln.reference_start
                ref_name=aln.reference_name

                revised_dict=dict()  #存储在primary query seq中，哪些位置添加了D或删除了I，从而导致长度改变

                for c in aln.cigartuples:
                    if c[0]==1:
                        if c[1]>=min_sv_size:
                            corrected_seq=corrected_seq+aln.query_sequence[current_read_pos:current_read_pos+c[1]]
                        else:
                            revised_dict[current_read_pos]=-c[1]
                        current_read_pos=current_read_pos+c[1]
                    elif c[0]==2:
                        if c[1]<min_sv_size:
                            corrected_seq=corrected_seq+ref_dict[ref_name][current_ref_pos:current_ref_pos+c[1]]
                            revised_dict[current_read_pos] = c[1]
                        current_ref_pos=current_ref_pos+c[1]
                    elif c[0]==0:
                        corrected_seq=corrected_seq+ref_dict[ref_name][current_ref_pos:current_ref_pos+c[1]]
                        current_ref_pos=current_ref_pos+c[1]
                        current_read_pos=current_read_pos+c[1]
                    elif c[0]==4:   #保留S区域，如果有SA，则根据SA的比对情况对S进行矫正
                        corrected_seq=corrected_seq+aln.query_sequence[current_read_pos:current_read_pos+c[1]]
                        current_read_pos=current_read_pos+c[1]

                # 根据 SA 矫正 PA 中 S 区域，只对primary alignment中的S矫正，novobreak过滤时只考虑primary的sequence
                if aln.has_tag('SA'):
                    corrected_seq=correct_S(corrected_seq,aln,join_SA,ref_dict[ref_name],revised_dict)
                transformed=transform(str(corrected_seq))
                fout.write(transformed+"\n")
                fname.write(aln.query_name+"\n")
    fout.close()
    fname.close()
    bam.close()
if __name__ == '__main__':

    # somatic_bam=sys.argv[1]
    # germline_bam=sys.argv[2]
    # ref_file=sys.argv[3]
    # output_dir=sys.argv[4]

    somatic_bam='/Users/duan/Desktop/results/somaticSV/test/somatic.bam'
    germline_bam='/Users/duan/Desktop/results/somaticSV/test/germline.bam'
    ref_file='/Users/duan/Downloads/data/ref/v38/chr20.fa'
    output_dir='/Users/duan/Desktop/results/somaticSV/test/'


    print("Start to correct somatic seq")
    correct_byRef(somatic_bam,ref_file,output_dir,'somatic')
    # print("Start to correct germline seq")
    # correct_byRef(germline_bam,ref_file,output_dir,'germline')
    # correct_byMD()

