import pysam
import sys
import os
import cigar
import numpy as np
from supplement import get_reverse_comp
def local_combine(sigs, candidate_ins_del, svtype, merge_threshold):
    if len(sigs)==0:
        return
    elif len(sigs)==1: #此时不需要merge
        candidate_ins_del.append(sigs[0])

    else:  #merge距离近的变异
        if svtype=='INS':
            temp_sig=sigs[0]
            temp_sig.append(sigs[0][0])
            for i in sigs[1:]:
                if i[0]-temp_sig[-1]<=merge_threshold:
                    temp_sig[1]+=i[1]
                    temp_sig[-1]=i[0]

                else:
                    candidate_ins_del.append([temp_sig[0],temp_sig[1],temp_sig[2]])
                    temp_sig=i
                    temp_sig.append(i[0])

            candidate_ins_del.append([temp_sig[0],temp_sig[1],temp_sig[2]])

        elif svtype=='DEL':
            temp_sig = sigs[0]
            #求一下删除变异的终点
            tmp_del_end=sigs[0][0]+sigs[0][1]
            temp_sig.append(tmp_del_end)
            for i in sigs[1:]:
                if i[0]-temp_sig[-1]<=merge_threshold:  #如果此变异的起点和上一个变异的终点距离过近
                    temp_sig[-1]=i[0]+i[1]
                    temp_sig[1]+=i[1]

                else:
                    candidate_ins_del.append([temp_sig[0], temp_sig[1], temp_sig[2]])
                    temp_sig=i
                    temp_sig.append(i[0]+i[1])

            candidate_ins_del.append([temp_sig[0], temp_sig[1], temp_sig[2]])



# def get_left_confusion(aln,i,ref_dict,ref_pos,query_pos):
#     # 计算断点左端的混乱度,1000个base的比对情况
#
#     if aln.reference_name not in ref_dict.keys():
#         return 0
#
#
#     ref_seq=ref_dict[aln.reference_name]
#     query_seq=aln.query_sequence
#     left = i - 1
#     left_INS_count = 0
#     left_Match_count = 0
#     left_DEL_count = 0
#     left_SUM_len = 0
#     left_Mismatch_count=0
#     while left >= 0:
#         left_t = aln.cigartuples[left]
#         left_SUM_len += left_t[1]
#         if left_SUM_len >= 1000:
#             cigar_len = left_t[1] - (left_SUM_len - 1000)
#         else:
#             cigar_len = left_t[1]
#
#         if left_t[0] == 0:
#             while cigar_len>0:
#                 if ref_seq[ref_pos]!=query_seq[query_pos]:
#                     left_Mismatch_count+=1
#                 else:
#                     left_Match_count+=1
#                 query_pos-=1
#                 ref_pos-=1
#                 cigar_len-=1
#         elif left_t[0] == 1:
#             if cigar_len <= 20:
#                 left_INS_count = left_INS_count + cigar_len
#             query_pos-=cigar_len
#         elif left_t[0] == 2:
#             if cigar_len <= 20:
#                 left_DEL_count = left_DEL_count + cigar_len
#             ref_pos-=cigar_len
#         if left_SUM_len >= 1000:
#             break
#         left = left - 1
#     left_confusion = (left_INS_count + left_DEL_count+left_Mismatch_count) / left_Match_count
#     return left_confusion


# def get_right_confusion(aln,i,ref_dict,ref_pos,query_pos):
#
#     if aln.reference_name not in ref_dict.keys():
#         return 0
#
#
#     ref_seq=ref_dict[aln.reference_name]
#     query_seq=aln.query_sequence
#     right = i + 1
#     right_INS_count = 0
#     right_Match_count = 0
#     right_DEL_count = 0
#     right_SUM_len = 0
#     right_Mismatch_count=0
#     while right < len(aln.cigartuples):
#         right_t = aln.cigartuples[right]
#         right_SUM_len += right_t[1]
#         if right_SUM_len >= 1000:
#             cigar_len = right_t[1] - (right_SUM_len - 1000)
#         else:
#             cigar_len = right_t[1]
#
#         if right_t[0] == 0:
#             right_Match_count = right_Match_count + cigar_len
#
#             while cigar_len>0:
#                 if ref_seq[ref_pos]!=query_seq[query_pos]:
#                     right_Mismatch_count+=1
#                     # if aln.query_name == 'C2_H1_32808':
#                     #     print(ref_pos,query_pos,ref_seq[ref_pos],query_seq[query_pos])
#                 else:
#                     right_Match_count+=1
#                 query_pos+=1
#                 ref_pos+=1
#                 cigar_len-=1
#
#
#         elif right_t[0] == 1:
#             if cigar_len <= 20:
#                 right_INS_count = right_INS_count + cigar_len
#             query_pos+=cigar_len
#         elif right_t[0] == 2:
#             if cigar_len <= 20:
#                 right_DEL_count = right_DEL_count + cigar_len
#             ref_pos+=cigar_len
#         if right_SUM_len >= 1000:
#             break
#         right = right + 1
#     right_confusion = (right_INS_count + right_DEL_count+right_Mismatch_count) / right_Match_count
#     return right_confusion


# def get_left_confusion_splits(ele,ref_dict,query_seq,read_name=""):
#     # if read_name == 'C2_H1_12191':
#     #     print("get_left")
#     if ele[4] not in ref_dict.keys():
#         return 0
#
#     ref_seq = ref_dict[ele[4]]
#     #将string转化为tuple
#     tuples=list(cigar.Cigar(ele[-1]).items())
#     # 计算断点左端的混乱度,1000个base的比对情况
#     if tuples[-1][1]!='S':
#         return 0
#
#     ref_pos=ele[3]-1
#     query_pos=ele[1]-1
#     left = len(tuples)-2
#     left_INS_count = 0
#     left_Match_count = 0
#     left_DEL_count = 0
#     left_SUM_len = 0
#     left_Mismatch_count =0
#     while left >= 0:
#         left_t = tuples[left]
#         left_SUM_len += left_t[0]
#         if left_SUM_len >= 1000:
#             cigar_len = left_t[0] - (left_SUM_len - 1000)
#         else:
#             cigar_len = left_t[0]
#         if left_t[1] == 'M':
#             while cigar_len>0:
#                 if ref_seq[ref_pos]!=query_seq[query_pos]:
#                     left_Mismatch_count+=1
#                 else:
#                     left_Match_count+=1
#
#                 # if read_name == 'C2_H1_12191':
#                 #     print(ref_pos,ref_seq[ref_pos],query_pos,query_seq[query_pos])
#                 query_pos-=1
#                 ref_pos-=1
#                 cigar_len-=1
#         elif left_t[1] == 'I':
#             if cigar_len <= 20:
#                 left_INS_count = left_INS_count + cigar_len
#             query_pos -= cigar_len
#         elif left_t[1] == 'D':
#             if cigar_len <= 20:
#                 left_DEL_count = left_DEL_count + cigar_len
#             ref_pos -= cigar_len
#         if left_SUM_len >= 1000:
#             break
#         left = left - 1
#     left_confusion = (left_INS_count + left_DEL_count+left_Mismatch_count) / left_Match_count
#     return left_confusion



# def get_right_confusion_splits(ele,ref_dict,query_seq,read_name=""):
#
#     if ele[4] not in ref_dict.keys():
#         return 0
#
#
#     # if read_name == 'C2_H1_47288':
#     #     print("get_right")
#     ref_seq = ref_dict[ele[4]]
#     # 将string转化为tuple
#     tuples = list(cigar.Cigar(ele[-1]).items())
#     # 计算断点左端的混乱度,1000个base的比对情况
#     if tuples[0][1] != 'S':
#         return 0
#
#     ref_pos=ele[2]
#     query_pos=ele[0]
#     right = 1
#     right_INS_count = 0
#     right_Match_count = 0
#     right_DEL_count = 0
#     right_SUM_len = 0
#     right_Mismatch_count=0
#     while right <len(tuples):
#         right_t = tuples[right]
#         right_SUM_len += right_t[0]
#         if right_SUM_len >= 1000:
#             cigar_len = right_t[0] - (right_SUM_len - 1000)
#         else:
#             cigar_len = right_t[0]
#
#         if right_t[1] == 'M':
#             right_Match_count = right_Match_count + cigar_len
#             while cigar_len>0:
#
#                 if ref_seq[ref_pos]!=query_seq[query_pos]:
#                     right_Mismatch_count+=1
#                 else:
#                     right_Match_count+=1
#                 # if read_name == 'C2_H1_47288':
#                 #     print(ref_pos,ref_seq[ref_pos],query_pos,query_seq[query_pos])
#                 query_pos+=1
#                 ref_pos+=1
#                 cigar_len-=1
#         elif right_t[1] == 'I':
#             if cigar_len <= 20:
#                 right_INS_count = right_INS_count + cigar_len
#         elif right_t[1] == 'D':
#             if cigar_len <= 20:
#                 right_DEL_count = right_DEL_count + cigar_len
#         if right_SUM_len >= 1000:
#             break
#         right= right + 1
#     right_confusion = (right_INS_count + right_DEL_count+right_Mismatch_count) / right_Match_count
#     return right_confusion


def analysis_alignment(aln,min_sv_len,ref_dict):
    query_pos=0
    ref_pos=aln.reference_start
    chro=aln.reference_name

    candidate_ins_del=list()
    aln_breakpoints  = list()
    #把同一个alignments中相邻的ins和del聚类合并成一个，并调整CIGAR！
    Combine_sig_in_same_read_ins=list()
    Combine_sig_in_same_read_del=list()

    merge_ins_threshold=100
    merge_del_threshold=0

    softclip_left=0
    softclip_right=0

    if aln.cigartuples[0][0] == 4:
        softclip_left = aln.cigartuples[0][1]
    if aln.cigar[-1][0] == 4:
        softclip_right = aln.cigartuples[-1][1]

    for i in range(len(aln.cigartuples)):
        t=aln.cigartuples[i]
        flag=t[0]
        counts=t[1]
        if flag==0:
            ref_pos=ref_pos+counts
            query_pos=query_pos+counts
        elif flag==4:
            query_pos=query_pos+counts
        elif flag==1:
            if counts>=min_sv_len:
                insert_start=query_pos
                insert_end=query_pos+counts
                if aln.is_reverse:
                    insert_start=aln.query_length-(query_pos+counts)
                    insert_end=aln.query_length-query_pos

                # left_confu=get_left_confusion(aln,i,ref_dict,ref_pos-1,query_pos-1)
                # right_confu=get_right_confusion(aln,i,ref_dict,ref_pos,query_pos+counts)
                left_confu=0
                right_confu=0
                aln_breakpoints.append([chro,'INS',ref_pos,counts,aln.query_name,aln.query_sequence[query_pos:query_pos+counts],insert_start,insert_end,left_confu,right_confu])
            query_pos=query_pos+counts
        elif flag==2:
            if counts>=min_sv_len:
                del_pos=query_pos
                if aln.is_reverse:
                    del_pos=aln.query_length-query_pos


                # left_confu=get_left_confusion(aln,i,ref_dict,ref_pos-1,query_pos-1)
                # right_confu=get_right_confusion(aln,i,ref_dict,ref_pos+counts,query_pos)
                left_confu=0
                right_confu=0
                aln_breakpoints.append([chro,'DEL',ref_pos, counts,aln.query_name,del_pos,del_pos,left_confu,right_confu])
                # Combine_sig_in_same_read_del.append([ref_pos, counts,'DEL'])
            ref_pos=ref_pos+counts

    # local_combine(Combine_sig_in_same_read_del,candidate_ins_del,'DEL',merge_del_threshold)
    # local_combine(Combine_sig_in_same_read_ins, candidate_ins_del, 'INS', merge_ins_threshold)
    #
    # aln_breakpoints=list()
    # #根据ref坐标排序
    # sorted(candidate_ins_del,key=lambda x:x[0])
    # #根据合并结果调整CIGAR,只关心S,M,I,D
    #
    # if len(candidate_ins_del)>=1:
    #     revised_cigarstr=""
    #     aln_ref_pos=aln.reference_start
    #
    #     if softclip_left!=0:
    #         revised_cigarstr+=str(softclip_left)+'S'
    #     for indel in candidate_ins_del:
    #
    #         M_counts=indel[0]-aln_ref_pos
    #         aln_ref_pos=indel[0]
    #         revised_cigarstr += str(M_counts)+'M'
    #
    #         if indel[2]=='INS':
    #             revised_cigarstr += str(indel[1]) + 'I'
    #         elif indel[2]=='DEL':
    #             revised_cigarstr += str(indel[1]) + 'D'
    #             aln_ref_pos+=indel[1]
    #
    #     #剩余的M个数
    #     last_M=aln.reference_end-aln_ref_pos
    #     revised_cigarstr += str(last_M)+'M'
    #
    #     if softclip_right!=0:
    #         revised_cigarstr+=str(softclip_right)+'S'
    #     # print(aln.reference_start, aln.reference_end,aln.cigarstring)
    #     aln.cigarstring=revised_cigarstr
    #     # print(aln.reference_start, aln.reference_end,aln.cigarstring)
    # #再根据新的cigarstring找变异
    #
    #
    # for t in aln.cigartuples:
    #     flag=t[0]
    #     counts=t[1]
    #     if flag==0:
    #         ref_pos=ref_pos+counts
    #         query_pos=query_pos+counts
    #     elif flag==4:
    #         query_pos=query_pos+counts
    #     elif flag==1:
    #         if counts>=min_sv_len:
    #             insert_start=query_pos
    #             insert_end=query_pos+counts
    #             if aln.is_reverse:
    #                 insert_start=aln.query_length-(query_pos+counts)
    #                 insert_end=aln.query_length-query_pos
    #             aln_breakpoints.append([chro,'INS',ref_pos,counts,aln.query_name,aln.query_sequence[query_pos:query_pos+counts],insert_start,insert_end])
    #             # Combine_sig_in_same_read_ins.append([ref_pos,counts,'INS'])
    #         query_pos=query_pos+counts
    #     elif flag==2:
    #         if counts>=min_sv_len:
    #             del_pos=query_pos
    #             if aln.is_reverse:
    #                 del_pos=aln.query_length-query_pos
    #             aln_breakpoints.append([chro,'DEL',ref_pos, counts,aln.query_name,del_pos,del_pos])
    #             # Combine_sig_in_same_read_del.append([ref_pos, counts,'DEL'])
    #         ref_pos=ref_pos+counts
    #
    #
    return aln_breakpoints





def acquire_clip_pos(deal_cigar):
    seq = list(cigar.Cigar(deal_cigar).items())
    if seq[0][1] == 'S':
        first_pos = seq[0][0]
    else:
        first_pos = 0
    if seq[-1][1] == 'S':
        last_pos = seq[-1][0]
    else:
        last_pos = 0
    bias = 0
    for i in seq:
        if i[1] == 'M' or i[1] == 'D' or i[1] == '=' or i[1] == 'X':
            bias += i[0]
    return [first_pos, last_pos, bias]

def retrieve_supp(aln):
    pos_start = aln.reference_start
    pos_end = aln.reference_end
    softclip_left = 0
    softclip_right = 0

    if aln.cigartuples[0][0] == 4:
        softclip_left = aln.cigartuples[0][1]
    if aln.cigartuples[-1][0] == 4:
        softclip_right = aln.cigartuples[-1][1]


    #如果比对到了正链
    if not aln.is_reverse:
        primary_info = [softclip_left, aln.query_length - softclip_right, pos_start,pos_end, aln.reference_name, '+',aln.cigarstring]
    else:
        primary_info = [softclip_right, aln.query_length - softclip_left, pos_start,pos_end, aln.reference_name, '-',cigar.Cigar(aln.cigarstring)._reverse_cigar()]


    split_reads=list()
    split_reads.append(primary_info)

    sa_tag = aln.get_tag("SA").split(";")

    # if aln.query_name=='m54336U_190829_230546/120719613/ccs':
    #     print(sa_tag)
    for sup_aln in sa_tag:
        fields = sup_aln.split(",")
        if len(fields) !=6:
            continue
        local_chr = fields[0]
        local_start = int(fields[1])-1
        local_cigar = fields[3]
        local_strand = fields[2]
        local_mapq = int(fields[4])
        if local_mapq >= 0:
            # if local_mapq >= 0:
            local_set = acquire_clip_pos(local_cigar)
            # if aln.query_name=='m54336U_190829_230546/120719613/ccs':
            #     print(local_start,local_set[2])
            if local_strand == '+':
                split_reads.append([local_set[0], aln.query_length - local_set[1], local_start,
                                   local_start + local_set[2], local_chr, local_strand,local_cigar])
            else:
                split_reads.append([local_set[1], aln.query_length - local_set[0], local_start,
                                       local_start + local_set[2], local_chr, local_strand,cigar.Cigar(local_cigar)._reverse_cigar()])

    return split_reads

def analysis_inv(ele_1, ele_2, read_name, sv_list, SV_size,ref_dict,read_len,query,reversed_query):
    chro=ele_1[4]
    if ele_1[5] == '+':
        # +-
        if ele_1[3] - ele_2[3] >= SV_size:
            if ele_2[0] + 0.5 * (ele_1[3] - ele_2[3]) >= ele_1[1]:
                # left_confu=get_right_confusion_splits(ele_2,ref_dict)
                # print(ele_1,ele_2,read_name,ele_2[3],ele_1[3])
                ele_2_reverse= [read_len - ele_2[1], read_len - ele_2[0]] + ele_2[2:-1]+[cigar.Cigar(ele_2[-1])._reverse_cigar()]
                # left_confu=get_left_confusion_splits(ele_2_reverse,ref_dict,reversed_query,read_name)
                left_confu=0


                sv_list.append([chro,"INV","++",ele_2[3],ele_1[3],read_name,ele_1[0],ele_2[0],left_confu,left_confu])  #测的负链

        if ele_2[3] - ele_1[3] >= SV_size:
            if ele_2[0] + 0.5 * (ele_2[3] - ele_1[3]) >= ele_1[1]:
                # left_confu=get_left_confusion_splits(ele_1,ref_dict)
                # print(ele_1,ele_2,read_name,ele_1[3],ele_2[3])
                # left_confu = get_left_confusion_splits(ele_1, ref_dict,query,read_name)
                left_confu=0
                sv_list.append([chro,"INV","++", ele_1[3],ele_2[3],read_name,ele_1[1],ele_2[1],left_confu,left_confu])  #测的正链
    else:
        # -+
        if ele_2[2] - ele_1[2] >= SV_size:
            if ele_2[0] + 0.5 * (ele_2[2] - ele_1[2]) >= ele_1[1]:
                # print(ele_1, ele_2, read_name, ele_1[2], ele_2[2])
                # right_confu = get_right_confusion_splits(ele_2,ref_dict,query,read_name)
                right_confu=0
                sv_list.append([chro,"INV","--", ele_1[2],ele_2[2],read_name,ele_1[0],ele_2[0],right_confu,right_confu])  #测的正链

        if ele_1[2] - ele_2[2] >= SV_size:

            if ele_2[0] + 0.5 * (ele_1[2] - ele_2[2]) >= ele_1[1]:
                # print(ele_1, ele_2, read_name, ele_2[2], ele_1[2])
                ele_1_reverse=[read_len - ele_1[1], read_len - ele_1[0]] + ele_1[2:-1]+[cigar.Cigar(ele_1[-1])._reverse_cigar()]
                # right_confu=get_right_confusion_splits(ele_1_reverse,ref_dict,reversed_query,read_name)
                right_confu=0
                sv_list.append([chro,"INV","--",ele_2[2],ele_1[2],read_name,ele_1[1],ele_2[1],right_confu,right_confu])  #测的负链

def analysis_split_read(split_reads,read_name,read_len,query,SV_size,ref_dict):
    '''
    read_start	read_end	ref_start	ref_end	chr	strand  cigar
    #0			#1			#2			#3		#4	#5  #6
    '''

    reversed_seq=get_reverse_comp(query)

    trigger_INS_TRA=0
    sv_list=list()
    sp_list = sorted(split_reads, key=lambda x: x[0])

    # if read_name=='C1_H1_17895':
    #     print(split_reads)
    #分析inversion
    if len(sp_list) == 2:
        ele_1 = sp_list[0]
        ele_2 = sp_list[1]
        if ele_1[4] == ele_2[4] and ele_1[5] != ele_2[5]:
            analysis_inv(ele_1,ele_2,read_name,sv_list,SV_size,ref_dict,read_len,query,reversed_seq)

    else:
        for a in range(len(sp_list[1:-1])):
            ele_1 = sp_list[a]
            ele_2 = sp_list[a + 1]
            ele_3 = sp_list[a + 2]

            if ele_1[4] == ele_2[4] == ele_3[4]:

                chro=ele_1[4]
                if ele_1[5] == ele_3[5] and ele_1[5] != ele_2[5]:
                    if ele_2[5] == '-':
                        # +-+
                        if ele_2[0] + 0.5 * (ele_3[2] - ele_1[3]) >= ele_1[1] and ele_3[0] + 0.5 * (ele_3[2] - ele_1[3]) >= ele_2[1]:
                            # left_confu=get_left_confusion_splits(ele_1,ref_dict,query)
                            # right_confu=get_right_confusion_splits(ele_3,ref_dict,query)
                            left_confu = 0
                            right_confu = 0
                            sv_list.append([chro,"INV","++",ele_1[3],ele_2[3],read_name,ele_1[1],ele_2[1],left_confu,right_confu])
                            sv_list.append([chro,"INV","--",ele_2[2],ele_3[2],read_name,ele_2[0],ele_3[0],left_confu,right_confu])
                    else:
                        # -+-
                        if ele_1[1] <= ele_2[0] + 0.5 * (ele_1[2] - ele_3[3]) and ele_3[0] + 0.5 * (ele_1[2] - ele_3[3]) >= ele_2[1]:
                            # No overlaps in split reads
                            ele_1_reverse = [read_len - ele_3[1], read_len - ele_3[0]] + ele_3[2:-1] + [
                                cigar.Cigar(ele_3[-1])._reverse_cigar()]
                            ele_3_reverse = [read_len - ele_1[1], read_len - ele_1[0]] + ele_1[2:-1] + [
                                cigar.Cigar(ele_1[-1])._reverse_cigar()]

                            # left_confu = get_left_confusion_splits(ele_1_reverse,ref_dict,reversed_seq)
                            # right_confu =get_right_confusion_splits(ele_3_reverse,ref_dict,reversed_seq)
                            left_confu = 0
                            right_confu = 0
                            sv_list.append([chro,"INV","++",ele_3[3],ele_2[3],read_name,ele_2[0],ele_3[0],left_confu,right_confu])
                            sv_list.append([chro,"INV","--",ele_2[2],ele_1[2],read_name,ele_1[1],ele_2[1],left_confu,right_confu])

                if ele_1[5] != ele_3[5]:
                    if ele_2[5] == ele_1[5]:
                        # ++-/--+
                        analysis_inv(ele_2,
                                     ele_3,
                                     read_name,
                                     sv_list,
                                     SV_size,ref_dict,read_len,query,reversed_seq)
                    else:
                        # +--/-++
                        analysis_inv(ele_1,
                                     ele_2,
                                     read_name,
                                     sv_list,
                                     SV_size,ref_dict,read_len,query,reversed_seq)


    #分析deletion,insertion,duplication
    for a in range(len(sp_list[:-1])):
        ele_1 = sp_list[a]
        ele_2 = sp_list[a + 1]
        if ele_1[4] == ele_2[4]:
            chro=ele_1[4]
            if ele_1[5] == ele_2[5]:
                # dup & ins & del
                if ele_1[5] == '-':
                    ele_1 = [read_len - sp_list[a + 1][1], read_len - sp_list[a + 1][0]] + sp_list[a + 1][2:-1]+[cigar.Cigar(sp_list[a + 1][-1])._reverse_cigar()]
                    ele_2 = [read_len - sp_list[a][1], read_len - sp_list[a][0]] + sp_list[a][2:-1]+[cigar.Cigar(sp_list[a][-1])._reverse_cigar()]
                    # 没有必要反转序列
                    # query = query[::-1]

                #read坐标全部按正链算

                if ele_1[3] - ele_2[2] >= SV_size and ele_1[3] - ele_2[2]<=10000:

                    dup_read_pos = int((ele_2[0] + ele_1[1]) / 2)
                    if ele_1[5] == '-':
                        dup_read_pos = read_len - dup_read_pos
                        # left_confu=get_left_confusion_splits(ele_1,ref_dict,reversed_seq,read_name)
                        # right_confu=get_right_confusion_splits(ele_2,ref_dict,reversed_seq,read_name)

                        left_confu = 0
                        right_confu = 0
                    else:
                        # left_confu=get_left_confusion_splits(ele_1,ref_dict,query,read_name)
                        # right_confu=get_right_confusion_splits(ele_2,ref_dict,query,read_name)

                        left_confu = 0
                        right_confu = 0
                    sv_list.append([chro,"DUP",ele_2[2],ele_1[3],read_name,dup_read_pos,dup_read_pos,left_confu,right_confu])
                if ele_1[3] - ele_2[2] < SV_size:
                    if ele_2[0] + ele_1[3] - ele_2[2] - ele_1[1] >= SV_size:
                        if ele_2[2] - ele_1[3] <= 100 and ele_2[0] + ele_1[3] - ele_2[2] - ele_1[1] <= 10000:

                            ins_read_pos1=ele_1[1]
                            ins_read_pos2=ele_2[0]
                            if ele_1[5]=='-':
                                ins_read_pos1=read_len-ele_2[0]
                                ins_read_pos2=read_len-ele_1[1]
                                # left_confu = get_left_confusion_splits(ele_1, ref_dict,reversed_seq,read_name)
                                # right_confu = get_right_confusion_splits(ele_2, ref_dict,reversed_seq,read_name)
                                left_confu = 0
                                right_confu = 0
                            else:
                                # left_confu=get_left_confusion_splits(ele_1,ref_dict,query,read_name)
                                # right_confu=get_right_confusion_splits(ele_2,ref_dict,query,read_name)
                                left_confu = 0
                                right_confu = 0
                            #int((ele_2[2] + ele_1[3]) / 2)
                            # print(read_name,ele_1,ele_2)
                            sv_list.append([chro,"INS",max(ele_2[2],ele_1[3]),
                                                               ele_2[0] + ele_1[3] - ele_2[2] - ele_1[1],
                                                               read_name,
                                                               str(query[
                                                                   ele_1[1] + int((ele_2[2] - ele_1[3]) / 2):
                                                                   ele_2[0] - int((ele_2[2] - ele_1[3]) / 2)]),ins_read_pos1,ins_read_pos2,left_confu,right_confu])
                    if ele_2[2] - ele_2[0] + ele_1[1] - ele_1[3] >= SV_size:
                        if ele_2[0] - ele_1[1] <= 100 and ele_2[2] - ele_2[0] + ele_1[1] - ele_1[3] <= 10000:

                            del_read_pos=int((ele_1[1]+ele_2[0])/2)
                            if ele_1[5]=='-':
                                del_read_pos=read_len-del_read_pos
                                # left_confu = get_left_confusion_splits(ele_1, ref_dict,reversed_seq,read_name)
                                # right_confu = get_right_confusion_splits(ele_2, ref_dict,reversed_seq,read_name)
                                left_confu = 0
                                right_confu = 0

                            else:
                                # left_confu=get_left_confusion_splits(ele_1,ref_dict,query)
                                # right_confu=get_right_confusion_splits(ele_2,ref_dict,query)
                                left_confu = 0
                                right_confu = 0
                            # print(read_name,ele_1,ele_2)
                            sv_list.append([chro,"DEL",ele_1[3],ele_2[2] - ele_2[0] + ele_1[1] - ele_1[3],read_name,del_read_pos,del_read_pos,left_confu,right_confu])
        else:
            trigger_INS_TRA = 1

    if len(sp_list) >= 3 and trigger_INS_TRA==1:
        if sp_list[0][4] == sp_list[-1][4]:
            if sp_list[0][5] != sp_list[-1][5]:
                pass
            else:
                if sp_list[0][5] == '+':
                    ele_1 = sp_list[0]
                    ele_2 = sp_list[-1]
                else:
                    ele_1 = [read_len - sp_list[-1][1], read_len - sp_list[-1][0]] + sp_list[-1][2:-1]+[cigar.Cigar(sp_list[-1][-1])._reverse_cigar()]
                    ele_2 = [read_len - sp_list[0][1], read_len - sp_list[0][0]] + sp_list[0][2:-1]+[cigar.Cigar(sp_list[0][-1])._reverse_cigar()]
                    query = query[::-1]

                # if read_name=='m64039_190922_223056/97387167/ccs':
                #     print(ele_1)
                #     print(ele_2)
                chro=ele_1[4]
                dis_ref = ele_2[2] - ele_1[3]
                dis_read = ele_2[0] - ele_1[1]
                if dis_ref < 100 and dis_read - dis_ref >= SV_size and dis_read - dis_ref <= 10000:
                    # print(min(ele_2[2], ele_1[3]), dis_read - dis_ref, read_name)
                    ins_read_pos1 = ele_1[1]
                    ins_read_pos2 = ele_2[0]
                    if ele_1[5] == '-':
                        ins_read_pos1 = read_len - ele_2[0]
                        ins_read_pos2 = read_len - ele_1[1]
                        # left_confu = get_left_confusion_splits(ele_1, ref_dict, reversed_seq)
                        # right_confu = get_right_confusion_splits(ele_2, ref_dict, reversed_seq)
                        left_confu = 0
                        right_confu = 0
                    else:
                        # left_confu = get_left_confusion_splits(ele_1, ref_dict, query)
                        # right_confu = get_right_confusion_splits(ele_2, ref_dict, query)
                        left_confu = 0
                        right_confu = 0
                    # print(ele_1,ele_2,read_name)
                    sv_list.append([chro,"INS",max(ele_2[2],ele_1[3]),dis_read - dis_ref,read_name,
                                    str(query[ele_1[1] + int(dis_ref / 2):ele_2[0] - int(dis_ref / 2)]),ins_read_pos1,ins_read_pos2,left_confu,right_confu])

                if dis_ref <= -SV_size:
                    dup_read_pos = ele_2[0] #dup前面还有别的变异，这种情况对右断点进行校验
                    if ele_1[5] == '-':
                        dup_read_pos = read_len - dup_read_pos
                        # left_confu = get_left_confusion_splits(ele_1, ref_dict, reversed_seq)
                        # right_confu = get_right_confusion_splits(ele_2, ref_dict, reversed_seq)
                        left_confu = 0
                        right_confu = 0
                    else:
                        # left_confu = get_left_confusion_splits(ele_1, ref_dict, query)
                        # right_confu = get_right_confusion_splits(ele_2, ref_dict, query)
                        left_confu = 0
                        right_confu = 0

                    # print(ele_1,ele_2,read_name)
                    sv_list.append([chro,"DUP",ele_2[2],ele_1[3],read_name,dup_read_pos,dup_read_pos,left_confu,right_confu])
    return sv_list

def refine_DEL(tmp_cluster,min_read_count,candidate_sv,min_sv_len,max_sv_len):

    #输入： pos, len, read_id,read_start,read_end,left_confu,right_confu
    #输出： pos,len,read_name_list,read_start_list,read_end_list,ref_start_list,len_list,mean_left_confu,mean_right_confu

    # 根据read_id去重，只保留len最大的记录
    dedup_reads = dict()
    for sv in tmp_cluster:
        if sv[2] not in dedup_reads:
            dedup_reads[sv[2]] = sv
        else:
            if sv[1] > dedup_reads[sv[2]][1]:
                dedup_reads[sv[2]] = sv

    if len(dedup_reads) < min_read_count:
        return

    #根据sv的长度排序
    sorted_dedup_reads = sorted(list(dedup_reads.values()), key=lambda x: x[1])
    sum_len = [i[1] for i in sorted_dedup_reads]
    distance_threhold = 0.5 * np.mean(sum_len)

    last_len = sorted_dedup_reads[0][1]

    refined=list()

    refined.append([[sorted_dedup_reads[0][0]], [sorted_dedup_reads[0][1]], [],
                           [sorted_dedup_reads[0][2]],[sorted_dedup_reads[0][3]],[sorted_dedup_reads[0][4]],
                    [sorted_dedup_reads[0][5]],[sorted_dedup_reads[0][6]]])

    for i in sorted_dedup_reads[1:]:

        #变异的长度不符合，新的变异
        if i[1] - last_len > distance_threhold:
            #计算上一个变异的support reads数
            refined[-1][2].append(len(refined[-1][0]))
            refined.append([[], [], [], [],[],[],[],[]])

        refined[-1][0].append(i[0])
        refined[-1][1].append(i[1])
        refined[-1][3].append(i[2])
        refined[-1][4].append(i[3])
        refined[-1][5].append(i[4])
        refined[-1][6].append(i[5])
        refined[-1][7].append(i[6])
        last_len = i[1]
    refined[-1][2].append(len(refined[-1][0]))

    #按照support reads数排序
    refined_sort = sorted(refined, key=lambda x: x[2])

    for cluster in refined_sort:
        if cluster[2][0]>=min_read_count:
            sv_start=np.mean(cluster[0])
            sv_len=np.mean(cluster[1])
            mean_left_confu=np.mean(cluster[6])
            mean_right_confu=np.mean(cluster[7])
            # if int(sv_start)==180027:
            #     print(cluster[0])
            #     print(cluster[6])
            #     print(cluster[7])
            if min_sv_len<=sv_len<=max_sv_len:
            #平均位置，平均长度，支持该变异的reads_name
                candidate_sv.append([int(sv_start),int(sv_len),cluster[3],cluster[4],cluster[5],cluster[0],cluster[1],
                                     mean_left_confu,mean_right_confu])

def cluster_DEL(sv_list,min_support,min_sv_len,max_sv_len):

    # del: chro,del,start,len,read_name,read_start,read_end,left_confusion,right_confusion

    max_cluster_bias=200
    read_count=min_support
    tmp_del_cluster = list()
    tmp_del_cluster.append([0,0,'',0,0])

    refined=list()

    for sv in sv_list:
        chro=sv[0]
        pos = int(sv[2])
        indel_len = int(sv[3])
        read_id = sv[4]
        read_start=sv[5]
        read_end=sv[6]
        left_confu=sv[7]
        right_confu=sv[8]
        #新的变异
        if pos - tmp_del_cluster[-1][0] > max_cluster_bias:

            # 考虑deletion的长度，对聚类后的结果进行细化，因为得到semi_del_cluster时只考虑了位置信息
            if len(tmp_del_cluster) >= read_count:
                if tmp_del_cluster[-1][0]!=0 and tmp_del_cluster[-1][1]!=0:
                    refine_DEL(tmp_del_cluster,read_count,refined,min_sv_len,max_sv_len)

            tmp_del_cluster = []
            tmp_del_cluster.append([pos, indel_len, read_id,read_start,read_end,left_confu,right_confu])
        else:
            tmp_del_cluster.append([pos, indel_len, read_id,read_start,read_end,left_confu,right_confu])

    if len(tmp_del_cluster) >= read_count:
        refine_DEL(tmp_del_cluster, read_count, refined,min_sv_len,max_sv_len)

    return refined

def refine_INS(tmp_cluster,min_read_count,candidate_sv,min_sv_len,max_sv_len):

    #输入：pos, len, read_id,ins_seq,read_start,read_end,left_confu,right_confu
    #输出：pos,len,read_name_list,ins_seq,read_start_list,read_end_list,ref_start_list,len_list,mean_left_confu,mean_right_confu
    # 根据read_id去重，只保留len最大的记录
    dedup_reads = dict()
    for sv in tmp_cluster:
        if sv[2] not in dedup_reads:
            dedup_reads[sv[2]] = sv
        else:
            if sv[1] > dedup_reads[sv[2]][1]:
                dedup_reads[sv[2]] = sv

    if len(dedup_reads) < min_read_count:
        return

    #根据sv的长度排序
    sorted_dedup_reads = sorted(list(dedup_reads.values()), key=lambda x: x[1])
    sum_len = [i[1] for i in sorted_dedup_reads]
    distance_threhold = 0.3 * np.mean(sum_len)

    last_len = sorted_dedup_reads[0][1]

    refined=list()
    refined.append([[sorted_dedup_reads[0][0]], [sorted_dedup_reads[0][1]], [],
                           [sorted_dedup_reads[0][2]],[sorted_dedup_reads[0][3]],[sorted_dedup_reads[0][4]],[sorted_dedup_reads[0][5]],
                    [sorted_dedup_reads[0][6]],[sorted_dedup_reads[0][7]]])

    for i in sorted_dedup_reads[1:]:

        #变异的长度不符合，新的变异
        if i[1] - last_len > distance_threhold:
            #计算上一个变异的support reads数
            refined[-1][2].append(len(refined[-1][0]))
            refined.append([[], [], [], [],[],[],[],[],[]])

        refined[-1][0].append(i[0])
        refined[-1][1].append(i[1])
        refined[-1][3].append(i[2])
        refined[-1][4].append(i[3])
        refined[-1][5].append(i[4])
        refined[-1][6].append(i[5])
        refined[-1][7].append(i[6])
        refined[-1][8].append(i[7])
        last_len = i[1]
    refined[-1][2].append(len(refined[-1][0]))

    #按照support reads数排序
    refined_sort = sorted(refined, key=lambda x: x[2])

    for cluster in refined_sort:
        if cluster[2][0]>=min_read_count:
            sv_start=np.mean(cluster[0])
            sv_len=np.mean(cluster[1])

            mean_left_confu=np.mean(cluster[7])
            mean_right_confu=np.mean(cluster[8])
            #平均位置，平均长度，支持该变异的reads_name,插入的序列
            if min_sv_len<=sv_len<=max_sv_len:
                candidate_sv.append([int(sv_start),int(sv_len),cluster[3],cluster[4][0],cluster[5],cluster[6],cluster[0],cluster[1],
                                     mean_left_confu,mean_right_confu])
            # print(candidate_sv[-1])

def cluster_INS(sv_list,min_support,min_sv_len,max_sv_len):
    # ins: chro,ins,start,len,read_name,ins_query,read_start,read_end,left_confu,right_confu

    max_cluster_bias = 100
    read_count = min_support
    tmp_ins_cluster = list()
    tmp_ins_cluster.append([0, 0, '', '',0, 0])

    refined = list()

    for sv in sv_list:
        pos = int(sv[2])
        indel_len = int(sv[3])
        read_id = sv[4]
        ins_seq=sv[5]
        read_start=sv[6]
        read_end=sv[7]

        left_confu=sv[8]
        right_confu=sv[9]
        # 新的变异
        if pos - tmp_ins_cluster[-1][0] > max_cluster_bias:

            # 考虑insertion的长度，对聚类后的结果进行细化，因为得到tmp_ins_cluster时只考虑了位置信息
            if len(tmp_ins_cluster) >= read_count:
                if tmp_ins_cluster[-1][0]!=0 and tmp_ins_cluster[-1][1]!=0:
                    refine_INS(tmp_ins_cluster, read_count, refined,min_sv_len,max_sv_len)

            tmp_ins_cluster = []
            tmp_ins_cluster.append([pos, indel_len, read_id,ins_seq,read_start,read_end,left_confu,right_confu])
        else:
            tmp_ins_cluster.append([pos, indel_len, read_id,ins_seq,read_start,read_end,left_confu,right_confu])

    if len(tmp_ins_cluster) >= read_count:
        refine_INS(tmp_ins_cluster, read_count, refined,min_sv_len,max_sv_len)

    return refined

def refine_DUP(tmp_cluster,min_read_count,candidate_sv,min_sv_len,max_sv_len):

    # 输入： start, end, read_name,read_start,read_end,left_confu,right_confu
    # 输出： start,len,read_name_list,read_start_list,read_end_list,ref_start_list,ref_end_list,mean_left_confu,mean_right_confu



    dedup_reads = dict()
    for sv in tmp_cluster:
        if sv[2] not in dedup_reads:
            dedup_reads[sv[2]] = sv

    if len(dedup_reads) < min_read_count:
        return
    tmp_cluster=list(dedup_reads.values())

    tmp_cluster.sort(key=lambda bk: (bk[0], bk[1]))

    #去重
    ref_start_list=list(i[0] for i in tmp_cluster)
    ref_end_list = list(i[1] for i in tmp_cluster)
    support_read = list(i[2] for i in tmp_cluster)
    read_start_list=list(i[3] for i in tmp_cluster)
    read_end_list = list(i[4] for i in tmp_cluster)
    left_confu_list = list(i[5] for i in tmp_cluster)
    right_confu_list = list(i[6] for i in tmp_cluster)
    if len(support_read) < min_read_count:
        return
    low_b = int(len(tmp_cluster) * 0.4)
    up_b = int(len(tmp_cluster) * 0.6)

    if low_b == up_b:
        breakpoint_1 = tmp_cluster[low_b][0]
        breakpoint_2 = tmp_cluster[low_b][1]
    else:
        breakpoint_1 = [i[0] for i in tmp_cluster[low_b:up_b]]
        breakpoint_2 = [i[1] for i in tmp_cluster[low_b:up_b]]
        breakpoint_1 = int(sum(breakpoint_1) / len(tmp_cluster[low_b:up_b]))
        breakpoint_2 = int(sum(breakpoint_2) / len(tmp_cluster[low_b:up_b]))

    mean_left_confu=np.mean(left_confu_list)
    mean_right_confu=np.mean(right_confu_list)

    if min_sv_len<=breakpoint_2-breakpoint_1<=max_sv_len:
        candidate_sv.append([breakpoint_1,breakpoint_2-breakpoint_1,support_read,read_start_list,read_end_list,ref_start_list,ref_end_list,
                             mean_left_confu,mean_right_confu])

def cluster_DUP(sv_list,min_support,min_sv_len,max_sv_len):
    # dup: chro, dup, start, end, read_name,read_start,read_end,left_confu,right_confu

    max_cluster_bias=500
    read_count=min_support

    tmp_dup_cluster = list()
    tmp_dup_cluster.append([0, 0, '', 0, 0])

    refined=list()
    for sv in sv_list:
        pos1=sv[2]
        pos2=sv[3]
        read_name=sv[4]
        read_start=sv[5]
        read_end=sv[6]
        left_confu=sv[7]
        right_confu=sv[8]
        if pos1 - tmp_dup_cluster[-1][0] > max_cluster_bias or pos2 - tmp_dup_cluster[-1][1] > max_cluster_bias:
            if len(tmp_dup_cluster) >= read_count:
                if tmp_dup_cluster[-1][0]!=0 and tmp_dup_cluster[-1][1]!=0:
                    refine_DUP(tmp_dup_cluster, read_count, refined,min_sv_len,max_sv_len)

            tmp_dup_cluster = []
            tmp_dup_cluster.append([pos1, pos2, read_name,read_start,read_end,left_confu,right_confu])
        else:
            tmp_dup_cluster.append([pos1, pos2, read_name,read_start,read_end,left_confu,right_confu])

    if len(tmp_dup_cluster) >= read_count:
        refine_DUP(tmp_dup_cluster,read_count,refined,min_sv_len,max_sv_len)

    return refined

def refine_INV(tmp_cluster,min_read_count,candidate_sv,min_sv_len,max_sv_len):

    #返回值：bk,len,read_name_list,read_start_list,read_end_list,ref_start_list,ref_end_list,mean_left_confu,mean_right_confu


    #输入：pos1,pos2,read_name,read_start,read_end,left_confu,right_confu

    max_cluster_bias=500
    read_id = [i[2] for i in tmp_cluster]
    support_read = len(list(set(read_id)))
    if support_read < min_read_count:
        return

    inv_cluster_b2 = sorted(tmp_cluster, key=lambda x: x[1])

    last_bp = inv_cluster_b2[0][1]
    temp_sum_b1 = inv_cluster_b2[0][0]
    temp_sum_b2 = last_bp
    temp_count = 1

    left_confu_sum=inv_cluster_b2[0][5]
    right_confu_sum = inv_cluster_b2[0][6]
    # max_sum = 0
    temp_id = dict()
    temp_id[inv_cluster_b2[0][2]] = [inv_cluster_b2[0][3],inv_cluster_b2[0][4]]
    ref_pos_recorder=dict()
    ref_pos_recorder[inv_cluster_b2[0][2]] = [inv_cluster_b2[0][0], inv_cluster_b2[0][1]]

    for i in inv_cluster_b2[1:]:
        if i[1] - last_bp > max_cluster_bias:
            if temp_count >= min_read_count:
                breakpoint_1 = round(temp_sum_b1 / temp_count)
                breakpoint_2 = round(temp_sum_b2 / temp_count)
                inv_len = breakpoint_2 - breakpoint_1

                mean_left_confu=round(left_confu_sum)/temp_count
                mean_right_confu=round(right_confu_sum)/temp_count

                max_count_id = len(temp_id)
                read_start_list=list(temp_id[key][0] for key in temp_id.keys())
                read_end_list=list(temp_id[key][1] for key in temp_id.keys())

                ref_start_list=list(ref_pos_recorder[key][0] for key in ref_pos_recorder.keys())
                ref_end_list = list(ref_pos_recorder[key][1] for key in ref_pos_recorder.keys())
                if inv_len >= min_sv_len and inv_len<=max_sv_len and max_count_id>=min_read_count:
                    candidate_sv.append([breakpoint_1,inv_len,list(temp_id.keys()),read_start_list,read_end_list,ref_start_list,ref_end_list,
                                         mean_left_confu,mean_right_confu])
            temp_id = dict()
            temp_count = 1
            temp_sum_b1 = i[0]
            temp_sum_b2 = i[1]
            temp_id[i[2]] = [i[3],i[4]]
            ref_pos_recorder[i[2]]=[i[0],i[1]]
            left_confu_sum=i[5]
            right_confu_sum=i[6]
        else:
            temp_count += 1
            temp_id[i[2]] = [i[3], i[4]]
            ref_pos_recorder[i[2]] = [i[0], i[1]]
            # if i[2] not in temp_id:
            #     temp_id[i[2]] = 0
            # else:
            #     temp_id[i[2]] += 1
            temp_sum_b1 += i[0]
            temp_sum_b2 += i[1]
            left_confu_sum+=i[5]
            right_confu_sum+=i[6]
        last_bp = i[1]
    if temp_count >= min_read_count:
        breakpoint_1 = round(temp_sum_b1 / temp_count)
        breakpoint_2 = round(temp_sum_b2 / temp_count)

        mean_left_confu = round(left_confu_sum) / temp_count
        mean_right_confu = round(right_confu_sum) / temp_count


        inv_len = breakpoint_2 - breakpoint_1
        read_start_list = list(temp_id[key][0] for key in temp_id.keys())
        read_end_list = list(temp_id[key][1] for key in temp_id.keys())
        max_count_id = len(temp_id)
        ref_start_list = list(ref_pos_recorder[key][0] for key in ref_pos_recorder.keys())
        ref_end_list = list(ref_pos_recorder[key][1] for key in ref_pos_recorder.keys())
        if inv_len >= min_sv_len and inv_len<=max_sv_len and max_count_id>=min_read_count:
            candidate_sv.append([breakpoint_1, inv_len, list(temp_id.keys()),read_start_list,read_end_list,ref_start_list,ref_end_list
                                 ,mean_left_confu,mean_right_confu])

def cluster_INV(sv_list,min_support,min_sv_len,max_sv_len):

    #inv: chro, inv, direction, start, end, read_name,read_start,read_end,left_confu,right_confu

    max_cluster_bias = 500
    read_count = min_support
    tmp_inv_cluster = list()
    tmp_inv_cluster.append([0, 0, '',0,0])

    refined = list()

    for sv in sv_list:

        pos1 = int(sv[3])
        pos2 = int(sv[4])
        read_name=sv[5]
        read_start=sv[6]
        read_end=sv[7]
        left_confu=sv[8]
        right_confu=sv[9]
        # 新的变异
        if pos1 - tmp_inv_cluster[-1][0] > max_cluster_bias or pos2 - tmp_inv_cluster[-1][1] > max_cluster_bias:

            # 考虑inversion的长度，对聚类后的结果进行细化，因为tmp_inv_cluster只考虑了位置信息
            if len(tmp_inv_cluster) >= read_count:
                if tmp_inv_cluster[-1][0]!=0 and tmp_inv_cluster[-1][1]!=0:
                    refine_INV(tmp_inv_cluster, read_count, refined,min_sv_len,max_sv_len)

            tmp_inv_cluster = []
            tmp_inv_cluster.append([pos1, pos2,read_name,read_start,read_end,left_confu,right_confu])
        else:
            tmp_inv_cluster.append([pos1, pos2,read_name,read_start,read_end,left_confu,right_confu])

    if len(tmp_inv_cluster) >= read_count:
        refine_INV(tmp_inv_cluster, read_count, refined,min_sv_len,max_sv_len)

    return refined

def get_breakpoints(bam_file,min_support=1,min_sv_len=50,max_sv_len=10000,min_map_qual=20,chro="",start=-1,end=-1,ref_dict=None):

    bam=pysam.AlignmentFile(bam_file,'r')

    breakpoints=list()


    record=open('/home/mzduan/somaticSV/COLO829_results/chr20/CNNSSV_record.txt','w')

    # record=open(wkdir+'/recorder.txt','w')

    if chro=="" and start==-1 and end==-1:
        alns=bam.fetch()
    else:
        alns=bam.fetch(contig=chro,start=start,end=end)

    for aln in alns:
        if aln.is_unmapped or aln.mapping_quality<min_map_qual:
            continue
        else:
            record.write('Query Name:\t'+aln.query_name+'\n')
            record.write('Query Reference Start:\t' + str(aln.reference_start) + '\n')
            record.flush()
            if aln.is_supplementary:   #对于supplementary，只分析alignment
                aln_breakpoints=analysis_alignment(aln,min_sv_len,ref_dict)
                breakpoints.extend(aln_breakpoints)
            else:   #对于primary，分析alignment和split

                aln_breakpoints=analysis_alignment(aln,min_sv_len,ref_dict)
                breakpoints.extend(aln_breakpoints)
                if aln.has_tag("SA"):
                    supps=retrieve_supp(aln)

                    if aln.is_reverse:
                        query=get_reverse_comp(aln.query_sequence)
                    else:
                        query=aln.query_sequence
                    split_breakpoints=analysis_split_read(supps,aln.query_name,aln.query_length,query,min_sv_len,ref_dict)
                    if split_breakpoints:
                        breakpoints.extend(split_breakpoints)


    bam.close()
    # # del: chro,del,start,len,read_name,read_start,read_end,left_confusion,right_confusion
    # # ins: chro,ins,start,len,read_name,ins_query,read_start,read_end,left_confusion,right_confusion
    # # inv: chro,inv,direction,start,end,read_name,read_start,read_end,left_confusion,right_confusion
    # # dup: chro,dup,start,end,read_name,read_start,read_end,left_confusion,right_confusion
    #
    #
    #
    #
    #将breakpoint排序再合并
    del_breakpoints=dict()
    ins_breakpoints=dict()
    dup_breakpoints=dict()
    inv_breakpoints=dict()

    for bk in breakpoints:
        if bk[1]=='INS':
            chro=bk[0]
            if chro in ins_breakpoints:
                ins_breakpoints[chro].append(bk)
            else:
                ins_breakpoints[chro]=list()
                ins_breakpoints[chro].append(bk)
        elif bk[1]=='INV':
            chro=bk[0]
            if chro in inv_breakpoints:
                inv_breakpoints[chro].append(bk)
            else:
                inv_breakpoints[chro]=list()
                inv_breakpoints[chro].append(bk)
        elif bk[1]=='DEL':
            chro=bk[0]
            if chro in del_breakpoints:
                del_breakpoints[chro].append(bk)
            else:
                del_breakpoints[chro]=list()
                del_breakpoints[chro].append(bk)
        elif bk[1]=='DUP':
            chro=bk[0]
            if chro in dup_breakpoints:
                dup_breakpoints[chro].append(bk)
            else:
                dup_breakpoints[chro]=list()
                dup_breakpoints[chro].append(bk)
    #按变异在ref上的位置排序


    for key in del_breakpoints.keys():
        del_breakpoints[key].sort(key=lambda bk: (bk[2],bk[3]))
    for key in ins_breakpoints.keys():
        ins_breakpoints[key].sort(key=lambda bk: (bk[2],bk[3]))
    for key in dup_breakpoints.keys():
        dup_breakpoints[key].sort(key=lambda bk: (bk[2],bk[3]))
    for key in inv_breakpoints.keys():
        inv_breakpoints[key].sort(key=lambda bk: (bk[3],bk[4]))


    cdel=dict()
    cins=dict()
    cinv=dict()
    cdup=dict()

    for key in del_breakpoints.keys():
        cdel[key]=cluster_DEL(del_breakpoints[key], min_support,min_sv_len,max_sv_len)
        # [[pos,len,[read_name_list]],...]
    for key in ins_breakpoints.keys():
        cins[key]=cluster_INS(ins_breakpoints[key],min_support,min_sv_len,max_sv_len)
        # [[pos,len,[read_name_list],insert_seq],...]
    for key in inv_breakpoints.keys():
        cinv[key]=cluster_INV(inv_breakpoints[key],min_support,min_sv_len,max_sv_len)
        # [[pos,len,[read_name_list],...]
    for key in dup_breakpoints.keys():
        cdup[key]=cluster_DUP(dup_breakpoints[key],min_support,min_sv_len,max_sv_len)
        # [[pos,len,[read_name_list],...]

    record.close()
    return cdel,cins,cinv,cdup,


if __name__ == '__main__':

    # bam_file=sys.argv[1]
    # work_dir=sys.argv[2]
    #
    # if os.path.exists(work_dir):
    #     print(work_dir+' is existed')
    #     raise Exception('Error')
    # else:
    #     os.mkdir(work_dir)

    bam_file='/Users/duan/Desktop/results/somaticSV/bam/CCS/0.5/somatic_bam_chr20/sim.srt.bam'
    work_dir='/Users/duan/Desktop/test/'

    min_support=1
    get_breakpoints(bam_file,min_support,work_dir)




