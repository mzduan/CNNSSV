def basecigar2str(base_cigar):
    c=base_cigar[0]
    count=1
    cigarstring=""
    for i in range(1,len(base_cigar)):
        if base_cigar[i]==c:
            count=count+1
        else:
            cigarstring=cigarstring+str(count)+base_cigar[i-1]
            count=1
            c=base_cigar[i]
    cigarstring=cigarstring+str(count)+c

    return cigarstring

def right_extend(right_alignment,left_ref_end):
    #转换成base cigar
    base_cigar=""
    for i in range(len(right_alignment.cigartuples)):
        if right_alignment.cigartuples[i][0] == 0:
            base_cigar = base_cigar + right_alignment.cigartuples[i][1]* 'M'
        elif right_alignment.cigartuples[i][0] == 1:
            base_cigar = base_cigar + right_alignment.cigartuples[i][1] * 'I'
        elif right_alignment.cigartuples[i][0] == 2:
            base_cigar = base_cigar + right_alignment.cigartuples[i][1] * 'D'
        elif right_alignment.cigartuples[i][0] == 4:
            base_cigar = base_cigar + right_alignment.cigartuples[i][1] * 'S'

    #找到query哪个位置比对到了left_ref_end

    ref_pos=right_alignment.reference_start
    query_pos=0
    for i in range(len(base_cigar)):
        # print(ref_pos,query_pos)
        c=base_cigar[i]
        if c=='S':
            query_pos=query_pos+1
        elif c=='I':
            query_pos=query_pos+1
        elif c=='D':
            if ref_pos==left_ref_end:
                partial_basecigar=base_cigar[i:]
                break
            ref_pos=ref_pos+1
        elif c=='M':
            if ref_pos==left_ref_end:
                partial_basecigar=base_cigar[i:]
                break
            ref_pos=ref_pos+1
            query_pos=query_pos+1

    partial_cigar=basecigar2str(partial_basecigar)
    return query_pos,partial_cigar

def is_cigar_support(aln,bk):
    query_pos=0
    ref_pos=aln.reference_start
    for t in aln.cigartuples:
        flag=t[0]
        counts=t[1]
        if flag==0:
            ref_pos=ref_pos+counts
            query_pos=query_pos+counts
        elif flag==4:
            query_pos=query_pos+counts
        elif flag==1:
            if counts>=50:
                if abs(ref_pos-bk[0])<=50 and abs(counts-bk[1])<=50:
                    # print(ref_pos)
                    return True
            query_pos=query_pos+counts
        elif flag==2:
            ref_pos=ref_pos+counts
    return False
def merge_insertion(to_merge,bk):

    #part1: 找出支持该insertion的split alignments，成对出现哦

    reads=dict()
    for aln in to_merge:
        if aln.query_name in reads.keys():
            reads[aln.query_name].append(aln)
        else:
            reads[aln.query_name]=[aln]
    split_support=dict()
    split_support_set=set()
    for k in reads.keys():
        if len(reads[k])==1:
            continue
        else:
            sorted(reads[k],key=lambda aln:aln.reference_start)
            candidate_split_support=list()
            for aln in reads[k]:
                if not is_cigar_support(aln,bk):
                    candidate_split_support.append(aln)
            for i in range(0,len(candidate_split_support)-1):
                l=candidate_split_support[i]
                r=candidate_split_support[i+1]
                if l.is_reverse==r.is_reverse:
                    insert_len=(r.query_alignment_start-l.query_alignment_end)-(r.reference_start-l.reference_end)
                    if insert_len>=50:
                        insert_pos=(r.reference_start+l.reference_end)/2
                        if abs(insert_pos-bk[0])<=50 and abs(insert_len-bk[1])<=50:
                            split_support[k]=[l,r]
                            split_support_set.add(l)
                            split_support_set.add(r)

    merged=list()
    for aln in to_merge:
        if aln not in split_support_set:
            merged.append(aln)


    for k in split_support.keys():
        left_alignment=split_support[k][0]
        right_alignment=split_support[k][1]
        left_ref_end=left_alignment.reference_end
        left_query_end=left_alignment.query_alignment_end
        right_ref_start=right_alignment.reference_start
        right_query_start=right_alignment.query_alignment_start

        # 把left_alignment的cigarstring右边的S去掉
        revised_cigar=""
        for i in range(len(left_alignment.cigartuples)-1):
            if left_alignment.cigartuples[i][0]==0:
                revised_cigar=revised_cigar+str(left_alignment.cigartuples[i][1])+'M'
            elif left_alignment.cigartuples[i][0]==1:
                revised_cigar=revised_cigar+str(left_alignment.cigartuples[i][1])+'I'
            elif left_alignment.cigartuples[i][0]==2:
                revised_cigar=revised_cigar+str(left_alignment.cigartuples[i][1])+'D'
            elif left_alignment.cigartuples[i][0]==4:
                revised_cigar=revised_cigar+str(left_alignment.cigartuples[i][1])+'S'
        #找到 这个read的哪个位置比对到了left_ref_end

        # 把right_alignment的cigar左边的S去掉
        clipped_right=""
        for i in range(1,len(right_alignment.cigartuples)):
            if right_alignment.cigartuples[i][0]==0:
                clipped_right=clipped_right+str(right_alignment.cigartuples[i][1])+'M'
            elif right_alignment.cigartuples[i][0]==1:
                clipped_right=clipped_right+str(right_alignment.cigartuples[i][1])+'I'
            elif right_alignment.cigartuples[i][0]==2:
                clipped_right=clipped_right+str(right_alignment.cigartuples[i][1])+'D'
            elif right_alignment.cigartuples[i][0]==4:
                clipped_right=clipped_right+str(right_alignment.cigartuples[i][1])+'S'


        # print(left_alignment.query_name,revised_cigar,clipped_right)
        if right_ref_start==left_ref_end:
            insert_len=right_query_start-left_query_end
            revised_cigar=revised_cigar+str(insert_len)+'I'+clipped_right
        elif right_ref_start<left_ref_end:
            right_query_start,right_cigarstring=right_extend(right_alignment,left_ref_end)
            insert_len = right_query_start - left_query_end
            revised_cigar=revised_cigar+str(insert_len)+'I'+right_cigarstring
        elif right_ref_start>left_ref_end:
            left_extend_len=right_ref_start-left_ref_end
            right_query_start=right_query_start-left_extend_len
            insert_len=right_query_start-left_query_end
            revised_cigar=revised_cigar+str(insert_len)+'I'+str(left_extend_len)+'M'+clipped_right


        left_alignment.cigarstring=revised_cigar


        merged.append(left_alignment)
    return merged

def tuple2cigar(cigartuple,j):
    cigarstring=""
    for i in range(j+1,len(cigartuple)):
        l=cigartuple[i]
        if l[0]==0:
            cigarstring=cigarstring+str(l[1])+'M'
        elif l[0]==1:
            cigarstring=cigarstring+str(l[1])+'I'
        elif l[0]==2:
            cigarstring=cigarstring+str(l[1])+'D'
        elif l[0]==4:
            cigarstring=cigarstring+str(l[1])+'S'
        elif l[0]==5:
            cigarstring=cigarstring+str(l[1])+'H'

    return cigarstring

def adjust_cigar(aln,insertion_start,j,insertion_len):
    # print(insertion_start)
    ins_left_base_cigar=""

    for i in range(j):
        if aln.cigartuples[i][0] == 0:
            ins_left_base_cigar = ins_left_base_cigar + aln.cigartuples[i][1] * 'M'
        elif aln.cigartuples[i][0] == 1:
            ins_left_base_cigar = ins_left_base_cigar + aln.cigartuples[i][1] * 'I'
        elif aln.cigartuples[i][0] == 2:
            ins_left_base_cigar = ins_left_base_cigar + aln.cigartuples[i][1] * 'D'
        elif aln.cigartuples[i][0] == 4:
            ins_left_base_cigar = ins_left_base_cigar + aln.cigartuples[i][1] * 'S'

    ref_pos=aln.reference_start
    query_pos=0
    for i in range(len(ins_left_base_cigar)):
        c=ins_left_base_cigar[i]
        # print(ref_pos,insertion_start)
        if c=='M':
            if ref_pos==insertion_start:
                partial_base_cigar=ins_left_base_cigar[0:i]
                partial_base_cigar=partial_base_cigar+insertion_len*'I'
                partial_base_cigar=partial_base_cigar+ins_left_base_cigar[i:]
                return basecigar2str(partial_base_cigar)
                break
            ref_pos=ref_pos+1
            query_pos=query_pos+1
        elif c=='I':
            query_pos=query_pos+1
        elif c=='D':
            if ref_pos==insertion_start:
                partial_base_cigar=ins_left_base_cigar[0:i]
                partial_base_cigar=partial_base_cigar+insertion_len*'I'
                partial_base_cigar=partial_base_cigar+ins_left_base_cigar[i:]
                return basecigar2str(partial_base_cigar)
                break
            ref_pos=ref_pos+1
        elif c=='S':
            query_pos=query_pos+1






def left_aligned_insertion(somatic_support_reads,germline_support_reads,bk):

    insertion_start=bk[0]
    left_insertion_pos = insertion_start
    sv_support_reads=list()
    sv_support_reads.extend(somatic_support_reads)
    sv_support_reads.extend(germline_support_reads)


    # all_cigar_list=[]

    for aln in sv_support_reads:
        ref_pos=aln.reference_start

        # cigar_list=[]

        for c in aln.cigartuples:
            # cigar_list.append([c[0],c[1]])
            if c[0]==0:
                ref_pos=ref_pos+c[1]
            elif c[0]==1:
                if c[1]>=50 and abs(ref_pos-insertion_start)<=50 and abs(c[1]-bk[1])<=50:
                    # print(aln.query_name,ref_pos)
                    left_insertion_pos=left_insertion_pos if left_insertion_pos<ref_pos else ref_pos
            elif c[0]==2:
                ref_pos=ref_pos+c[1]
        # all_cigar_list.append(cigar_list)


    revised_somatic_support_reads=list()
    revised_germline_support_reads=list()

    boundary=len(somatic_support_reads)


    for i in range(len(sv_support_reads)):
        aln=sv_support_reads[i]
        revised_cigarstring=None
        # cigar_list=all_cigar_list[i]

        ref_pos=aln.reference_start
        query_pos=0

        for j in range(len(aln.cigartuples)):
            if aln.cigartuples[j][0]==1:
                if aln.cigartuples[j][1]>=50 and abs(ref_pos-insertion_start)<=50 and abs(aln.cigartuples[j][1]-bk[1])<=50:
                    if ref_pos-left_insertion_pos>0:
                        left_cigar=adjust_cigar(aln, left_insertion_pos, j,aln.cigartuples[j][1])
                        right_cigar=tuple2cigar(aln.cigartuples,j)
                        revised_cigarstring=left_cigar+right_cigar
                    break
                query_pos=query_pos+aln.cigartuples[j][1]
            elif aln.cigartuples[j][0]==0:
                ref_pos=ref_pos+aln.cigartuples[j][1]
                query_pos=query_pos+aln.cigartuples[j][1]
            elif aln.cigartuples[j][0]==2:
                ref_pos = ref_pos + aln.cigartuples[j][1]
            elif aln.cigartuples[j][0]==4:
                query_pos=query_pos+aln.cigartuples[j][1]
        # revised_cigarstring=tuple2cigar(cigar_list)
        if revised_cigarstring:
            aln.cigarstring=revised_cigarstring
        if i<boundary:
            revised_somatic_support_reads.append(aln)
        else:
            revised_germline_support_reads.append(aln)
    return revised_somatic_support_reads,revised_germline_support_reads,left_insertion_pos