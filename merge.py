def merge_seq_direction(seq1,seq2,zero):
    seq_len=len(seq1)
    merged_seq=""
    for i in range(seq_len):
        c1=seq1[i]
        c2=seq2[i]
        if c1==zero and c2==zero:
            merged_seq=merged_seq+zero
        elif c1!=zero and c2==zero:
            merged_seq=merged_seq+c1
        elif c1==zero and c2!=zero:
            merged_seq=merged_seq+c2
        elif c1!=zero and c2!=zero:
            merged_seq = merged_seq + c1
    return merged_seq
# def merge_basequal_mapq(qual_list1,qual_list2):
#     merged_qual=list()
#     for i in range(len(qual_list1)):
#         q1=qual_list1[i]
#         q2=qual_list2[i]
#         if q1=='0' and q2=='0':
#             merged_qual.append('0')
#         elif q1!='0' and q2=='0':
#             merged_qual.append(q1)
#         elif q1=='0' and q2!='0':
#             merged_qual.append(q2)
#         elif q1!='0' and q2!='0':
#             merged_qual.append(q1)
#     return merged_qual

def merge_depth(depth1,depth2):
    seq_len=len(depth1)
    merged_depth=""
    for i in range(seq_len):
        d1=int(depth1[i])
        d2=int(depth2[i])
        # merged=d1+d2
        # merged_depth=merged_depth+str(merged)
        if d1==0 and d2==0:
            merged_depth=merged_depth+'0'
        elif d1==1 and d2==1:
            merged_depth=merged_depth+'2'
        else:
            merged_depth=merged_depth+'1'
    return merged_depth

def merge_same_read(read_seq_list,read_direction_list,read_depth_list,read_name_list):
    name2column={}
    pos=3
    to_delete=list()
    for i in range(len(read_name_list)):
        if read_name_list[i] in name2column.keys():
            name2column[read_name_list[i]].append(pos)
        else:
            name2column[read_name_list[i]]=[pos]
        pos=pos+1

    for k in name2column.keys():
        if len(name2column[k])>=2:
            for i in range(1,len(name2column[k])):
                merged_seq = merge_seq_direction(read_seq_list[name2column[k][0]], read_seq_list[name2column[k][i]],'-')
                read_seq_list[name2column[k][0]]=merged_seq


                merged_direction = merge_seq_direction(read_direction_list[name2column[k][0]], read_direction_list[name2column[k][i]],'0')
                read_direction_list[name2column[k][0]]=merged_direction
                # print(read_depth_list[name2column[k][0]])
                # print(read_depth_list[name2column[k][i]])
                merged_depth = merge_depth(read_depth_list[name2column[k][0]], read_depth_list[name2column[k][i]])
                # print(merged_depth)
                # print(' ')
                read_depth_list[name2column[k][0]]=merged_depth

                # merged_basequal=merge_basequal_mapq(read_basequal_list[name2column[k][0]],read_basequal_list[name2column[k][i]])
                # read_basequal_list[name2column[k][0]] = merged_basequal


                to_delete.append(name2column[k][i])
    #合并后，删除多余的seq,按从大到小的顺序删除，不会出错
    to_delete.sort(reverse=True)

    for i in to_delete:
        del read_seq_list[i]
        del read_direction_list[i]
        del read_depth_list[i]
        # del read_basequal_list[i]
        del read_name_list[i-3]




    return read_seq_list,read_direction_list,read_depth_list