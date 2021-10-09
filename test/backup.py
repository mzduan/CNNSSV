# def up_sample(bk1,bk2,seq_list,direction_list,depth_list):
#
#     sv_len=bk2-bk1
#     sv_pos=range(bk1,bk2)
#     extend_length=400-sv_len
#     extend_pos=np.random.choice(sv_pos,size=extend_length,replace=True)
#
#     for i in range(len(seq_list)):
#
#         extend_seq = ""
#         extend_direction = ""
#         extend_depth = ""
#
#         seq=seq_list[i]
#         direction=direction_list[i]
#         depth=depth_list[i]
#
#         for pos in extend_pos:
#             extend_seq=extend_seq+seq[pos]
#             extend_direction=extend_direction+direction[pos]
#             extend_depth=extend_depth+depth[pos]
#
#         seq_list[i]=seq[0:bk2]+extend_seq+seq[bk2:]
#         direction_list[i]=direction[0:bk2]+extend_direction+extend_direction[bk2:]
#         depth_list[i]=depth[0:bk2]+extend_depth+depth[bk2:]
#
#     return seq_list,direction_list,depth_list


#调整到高度为50
# def unify_height(seq_list,direction_list,depth_list,sv_support_reads,ref_support_reads):
#
#     original_height=len(seq_list)
#     sample_start=1
#
#     sample_range=range(sample_start,original_height)
#
#
#     if original_height<50:  #上采样
#         sample_counts=50-original_height
#         sample_column=np.random.choice(sample_range,sample_counts,replace=True)
#
#         sorted_sample_column = sorted(sample_column, reverse=True)
#         for i in sorted_sample_column:
#             if i<=sv_support_reads:
#                 seq_list.insert(sv_support_reads+1,seq_list[i])
#                 direction_list.insert(sv_support_reads+1,direction_list[i])
#                 depth_list.insert(sv_support_reads+1, depth_list[i])
#             else:
#                 seq_list.append(seq_list[i])
#                 direction_list.append(direction_list[i])
#                 depth_list.append(depth_list[i])
#
#     elif original_height>50: #下采样
#         sample_counts=50
#         sample_column=np.random.choice(sample_range,sample_counts,replace=False)
#
#         sorted_sample_column=sorted(sample_column,reverse=True)
#         for c in sorted_sample_column:
#             del seq_list[c]
#             del direction_list[c]
#             del depth_list[c]
#
#     return seq_list,direction_list,depth_list



# def correct_byMD():
#     k_size=31
#
#
#     # fout=open('/home/yelab/dmz/somaticSV/data/germline_bam/germline_corrected.txt','w')
#     # fout_read_name=open('/home/yelab/dmz/somaticSV/data/germline_bam/germline_readname.txt','w')
#     fout=open('/Users/duan/Desktop/test.txt','w')
#     fout_read_name=open('/Users/duan/Desktop/test_name.txt','w')
#
#     # ref_dict=reference.initial_fa('/home/yelab/dmz/somaticSV/human_ref/chr20.fa')
#     # bam=pysam.AlignmentFile('/home/yelab/dmz/somaticSV/data/germline_bam/sim.srt.bam','r')
#     ref_dict = reference.initial_fa('/Users/duan/Downloads/data/ref/v38/chr20.fa')
#     bam=pysam.AlignmentFile('/Users/duan/Desktop/results/somaticSV/novoBreak/data_15000bp/bam/somatic.bam','r')
#
#     # counts=0
#
#     for aln in bam:
#
#         # if counts%1000==0:
#         #     print(str(counts)+"\talignments have been corrected")
#         #
#         # counts=counts+1
#         if aln.is_unmapped or aln.mapping_quality<=20:
#             continue
#         elif aln.query_length < k_size+3:
#             continue
#
#         quality = aln.query_qualities
#         lowq_num = 0
#         for i in range(len(quality)):
#             if quality[i]+33<=ord('#'):
#                 lowq_num=lowq_num+1
#         if float(lowq_num)/len(quality) >= 0.5:
#             continue
#         else:
#
#             fout_read_name.write(aln.query_name+"\n")
#             read_seq = aln.query_sequence
#             # print(read_seq)
#             read_pos = 0
#             ref_pos = aln.reference_start
#
#             #先删掉所有I
#             large_I=[]   #存储 大于等于50bp的 insertion
#             I_pos = []
#             I_pos.append(0)
#             for c in aln.cigartuples:
#                 if c[0] == 0:
#                     read_pos = read_pos + c[1]
#                 elif c[0] == 1:
#                     I_pos.append(read_pos)
#                     I_pos.append(read_pos + c[1])
#                     if c[1] >= 50:
#                         I_seq=read_seq[read_pos:read_pos+c[1]]
#                         large_I.append(I_seq)
#                     read_pos = read_pos + c[1]
#                 elif c[0] == 4:    #S可能是duplication，不能去掉
#                     read_pos = read_pos + c[1]
#             I_pos.append(read_pos)
#
#             large_I_pos_in_withoutI = []
#             read_seq_withoutI = ""
#             for i in range(0, len(I_pos), 2):
#                 if i>0 and I_pos[i]-I_pos[i-1]>=50:
#                     large_I_pos_in_withoutI.append(len(read_seq_withoutI))
#                 read_seq_withoutI = read_seq_withoutI + read_seq[I_pos[i]:I_pos[i + 1]]
#
#             # print(read_seq_withoutI)
#             # print(large_I_pos_in_withoutI)
#
#
#             read_seq_withoutI = list(read_seq_withoutI)
#             if aln.has_tag('MD'):
#                 MD_str=aln.get_tag('MD')
#                 #处理MD:  D补上，mismatch按ref走,此时MD的坐标对应到删除S和I后的read_seq_withoutI
#                 #先处理snp
#                 without_D=re.sub('\^[A-Z]+'," ",MD_str)   #得到不包含D的片段
#                 D_pos=[]     #记录从何处开始
#                 if aln.cigartuples[0][0]==4:
#                     read_pos=aln.cigartuples[0][1]
#                 else:
#                     read_pos=0
#                 tmp_digit=""
#                 for i in range(len(without_D)):
#                     if without_D[i]>='0' and without_D[i]<='9':
#                         tmp_digit=tmp_digit+without_D[i]
#                     elif without_D[i]==" ":
#                         Mcounts=int(tmp_digit)
#                         read_pos=read_pos+Mcounts
#                         D_pos.append(read_pos)
#                         tmp_digit=""
#                     elif without_D[i]>='A' and without_D[i]<='Z':   #mismatch
#                         Mcounts=int(tmp_digit)
#                         read_pos=read_pos+Mcounts
#                         tmp_digit=""
#                         read_seq_withoutI[read_pos]=without_D[i]
#                         read_pos=read_pos+1
#                 read_seq_withoutI=''.join(read_seq_withoutI)
#
#
#                 #再处理D，把D给补上
#                 D_pos_len={}
#                 D_str=re.findall('\^[A-Z]+',MD_str)
#                 if len(D_pos)!=len(D_str):
#                     raise Exception("Invalid D pos")
#                 #key : pos  ,  value: length of the deletion
#                 for i in range(len(D_pos)):
#                     if len(D_str[i][1:])<50:
#                         D_pos_len[D_pos[i]]=len(D_str[i][1:])
#
#                 read_seq_withD=""
#                 current_D_pos=0
#                 for i in range(len(D_pos)):
#                     read_seq_withD=read_seq_withD+read_seq_withoutI[current_D_pos:D_pos[i]]
#                     current_D_pos=D_pos[i]
#                     if len(D_str[i][1:])<50:
#                         read_seq_withD=read_seq_withD+D_str[i][1:]
#                 read_seq_withD=read_seq_withD+read_seq_withoutI[current_D_pos:]
#
#                 # print(read_seq_withD)
#
#
#                 #把大于50bp的insertion还原回去,需要使用 D_pos_len
#                 sorted(D_pos_len.items(),key = lambda item: item[0])
#
#                 #找到大的insertion在 加上小D后的序列上的坐标
#                 list_keys=list(D_pos_len.keys())
#                 large_I_pos_in_withD=[]
#                 for p in large_I_pos_in_withoutI:
#                     index=bisect.bisect_left(list_keys,p)
#                     diviation=0
#                     for i in range(index):
#                         diviation=diviation+D_pos_len[list_keys[i]]
#
#                     large_I_pos_in_withD.append(p+diviation)
#
#                 # print(large_I_pos_in_withD)
#                 # print(large_I)
#
#                 #把大的insertion加上，
#                 read_seq_withD_largeI=""
#                 current_pos=0
#                 for i in range(len(large_I_pos_in_withD)):
#                     read_seq_withD_largeI=read_seq_withD_largeI+read_seq_withD[current_pos:large_I_pos_in_withD[i]]
#                     read_seq_withD_largeI=read_seq_withD_largeI+large_I[i]
#                     current_pos=large_I_pos_in_withD[i]
#                 read_seq_withD_largeI=read_seq_withD_largeI+read_seq_withD[current_pos:]
#
#
#                 transformed=transform(read_seq_withD_largeI)
#                 fout.write(transformed+"\n")
#                 # fout.write(read_seq_withD + "\n")
#                 # print(read_seq_withD_largeI)
#                 # print(ref_dict[aln.reference_name][aln.reference_start:aln.reference_start+len(read_seq_withD)])
#
#             else:
#
#                 transformed = transform(read_seq_withoutI)
#
#                 # fout.write(read_seq_withoutI)
#                 fout.write(transformed+"\n")
#                 # print(read_seq_withoutI)
#                 # print(ref_dict[aln.reference_name][aln.reference_start:aln.reference_start+len(read_seq_withD)])
#
#
#     bam.close()
#     fout.close()
#     fout_read_name.close()



# def retrieve_supplementary_alignments(aln):
#     # if aln.query_name == 'C2_H1_28117':
#     #     print(aln.query_name)
#
#     #根据primary alignment计算原始 reads的长度  primary中只包含S不包含H
#     query_length=0
#     for t in aln.cigartuples:
#         if t[0]==4:
#             query_length=query_length+t[1]
#         elif t[0]==0 or t[0]==1:
#             query_length=query_length+t[1]
#
#     sa_tag = aln.get_tag("SA").split(";")
#     supplementary_aligns = list()
#     for sup_aln in sa_tag:
#         fields = sup_aln.split(",")
#         if len(fields) !=6:
#             continue
#         sup_aln_chr=fields[0]
#         sup_aln_start = int(fields[1])-1    # 1-based
#         sup_aln_direction=fields[2]
#         sup_aln_cigar=fields[3]
#
#         #将cigarstring转为tuple
#         i = 0
#         cigar_tuples = list()
#         for j in range(len(sup_aln_cigar)):
#             if sup_aln_cigar[j] >= '0' and sup_aln_cigar[j] <= '9':
#                 continue
#             else:
#                 cigar_tuples.append((int(sup_aln_cigar[i:j]), sup_aln_cigar[j]))
#                 i = j + 1
#
#         sup_aln_end = get_sup_aln_end(sup_aln_start, cigar_tuples)
#         #sup_aln_start,sup_aln_end: sup在ref上比对的坐标
#
#         #sup_read_start, sup_read_end:  sup在read上的坐标
#         sup_read_start=0
#         if cigar_tuples[0][1]=='H' or cigar_tuples[0][1]=='S':
#             sup_read_start=cigar_tuples[0][0]
#
#         sup_read_end=sup_read_start
#         for i in range(len(cigar_tuples)):
#             if cigar_tuples[i][1]=='I':
#                 sup_read_end = sup_read_end+cigar_tuples[i][0]
#             elif cigar_tuples[i][1]=='M':
#                 sup_read_end = sup_read_end + cigar_tuples[i][0]
#
#
#         #记录sup的比对信息：chr, ref_start, ref_end, read_start, read_end, cigar, direction, q_length, is_primary?
#         supplementary_aligns.append([sup_aln_chr,sup_aln_start,sup_aln_end,sup_read_start,sup_read_end,sup_aln_cigar,sup_aln_direction,query_length,False,aln.query_name])
#
#     aln_direction='-' if aln.is_reverse else '+'
#     supplementary_aligns.append([aln.reference_name, aln.reference_start, aln.reference_end, aln.query_alignment_start,aln.query_alignment_end,aln.cigarstring, aln_direction,query_length,True,aln.query_name])
#
#     # supplementary_aligns.sort(key=lambda aln: (aln[3]))
#     primary_direction=""
#     for i in range(len(supplementary_aligns)):
#         aln=supplementary_aligns[i]
#         if aln[8]== True:
#             primary_direction=aln[6]
#     for i in range(len(supplementary_aligns)):
#         aln=supplementary_aligns[i]
#         if aln[6]!=primary_direction:
#             tmp_aln3=aln[3]
#             tmp_aln4=aln[4]
#             aln[3]=aln[7]-tmp_aln4
#             aln[4]=aln[7]-tmp_aln3
#
#     supplementary_aligns.sort(key=lambda aln: (aln[3]))
#     # if supplementary_aligns[0][-1] == 'C2_H1_28117':
#     #     print(supplementary_aligns)
#     return supplementary_aligns


# def get_sup_aln_end(start,cigar_tuples):
#
#     end=start
#     for t in cigar_tuples:
#         flag=t[1]
#         counts=t[0]
#         if flag=='M':
#             end=end+counts
#         elif flag=='D':
#             end=end+counts
#         else:
#             continue
#     return end


# def get_reverse_seq(seq):
#     reverse_seq=""
#     for i in range(len(seq)-1,-1,-1):
#         if seq[i]=='A':
#             reverse_seq=reverse_seq+'T'
#         elif seq[i]=='T':
#             reverse_seq=reverse_seq+'A'
#         elif seq[i]=='C':
#             reverse_seq=reverse_seq+'G'
#         elif seq[i]=='G':
#             reverse_seq=reverse_seq+'C'
#         elif seq[i]=='N':
#             reverse_seq=reverse_seq+'N'
#     return reverse_seq



# def analysis_split(supps):
#
#
#     split_breakpoints=list()
#
#
#     #step1 : 按primary alignment,调整各sup的在reads上的坐标
#
#     #step2 : 按照ref上的顺序，从小到大，依次考察相邻两个alignments
#     for i in range(len(supps)-1):
#         aln1=supps[i]
#         aln2=supps[i+1]
#         if aln1[0]==aln2[0]:  #如果比对到了同一个染色体上
#             chro=aln1[0]
#             ref_distance=aln2[1]-aln1[2]
#             if aln1[6]==aln2[6]:  #比对方向一致
#                 read_distance=aln2[3]-aln1[4]
#                 if read_distance>-10:   #在read上无overlap
#                     if ref_distance>=-10:   #在ref上无overlap，排除dup
#                         diversion=read_distance-ref_distance
#                         if diversion>=50:  #insertion
#                             # if(aln1[-1]=='C2_H1_4951'):
#                             #     print(aln1[1],aln1[2],aln1[3],aln1[4],aln2[1],aln2[2],aln2[3],aln2[4],diversion)
#                             split_breakpoints.append( (chro ,aln1[2],aln1[2],'INS',aln1[-1]))
#                         elif diversion<=-50: #deletion
#                             split_breakpoints.append((chro,aln1[2], aln2[1], 'DEL'))
#                     else:
#                         if ref_distance<=-50: #dup
#                             split_breakpoints.append((chro,aln2[1],aln1[2],'DUP'))
#
#             else:
#
#                 #if two dup are very close to each other, we will miss this situation ( 1 PA 5 SA )
#                 if len(supps) == 3:
#                     # if supps[0][-1]=='C2_H1_23939':
#                     #     print(supps)
#                     #     print(supps[1][1],supps[0][2],supps[2][1],supps[1][2],supps[1][3],supps[0][4],supps[2][3],supps[1][4])
#                     #  inversion
#                     if abs(supps[1][1]-supps[0][2])<=20 and abs(supps[2][1]-supps[1][2])<=20 and abs(supps[1][3]-supps[0][4])<=20 and abs(supps[2][3]-supps[1][4])<=20:
#                         # if supps[0][-1] == 'C2_H1_23939':
#                         #     print(supps)
#                         split_breakpoints.append((chro,supps[1][1],supps[1][2],'INV'))
#                     break
#
#
#         # translocation 模块暂未实现
#         # else:
#     return split_breakpoints


#最原始的聚类算法
# breakpoints=list()
# breakpoints.extend(del_breakpoints)
# breakpoints.extend(ins_breakpoints)
# breakpoints.extend(dup_breakpoints)
# breakpoints.extend(inv_breakpoints)


# i=0
# while True:
#
#     if(i==len(breakpoints)):
#         break
#     for j in range(i,len(breakpoints)):
#
#         if breakpoints[i][3]==breakpoints[j][3] and abs(breakpoints[i][1]-breakpoints[j][1]) <=20 and abs(breakpoints[i][2]-breakpoints[j][2])<=20:
#             if j==len(breakpoints)-1:
#                 merged_pair=(i,j)
#                 i=j
#                 merged_breakpoints_pair.append(merged_pair)
#         else:
#             merged_pair=(i,j-1)
#             i=j-1
#             merged_breakpoints_pair.append(merged_pair)
#             break
#     i=i+1
# for iter in merged_breakpoints_pair:
#     bk=breakpoints[iter[0]]
#     if (iter[1]-iter[0]+1)>=2:
#         merged_breakpoints.append((bk,iter[1]-iter[0]+1))
# print("Candidate SVs(support=2):\t",len(merged_breakpoints))
# return merged_breakpoints


# with open(work_dir + 'DEL.txt', 'w') as fout:
#     for bk in cdel:
#         start = str(bk[0])
#         # sv_len=str(bk[1])
#         end = str(bk[0] + bk[1])
#         fout.write('DEL' + '\t' + start + '\t' + end)
#         for qname in bk[2]:
#             fout.write('\t' + qname)
#         fout.write('\n')
# with open(work_dir + 'INS.txt', 'w') as fout:
#     for bk in cins:
#         start = str(bk[0])
#         # sv_len=str(bk[1])
#         end = str(bk[0] + 1)
#         fout.write('INS' + '\t' + start + '\t' + end)
#         for qname in bk[2]:
#             fout.write('\t' + qname)
#         fout.write('\n')
# with open(work_dir + 'DUP.txt', 'w') as fout:
#     for bk in cinv:
#         start = str(bk[0])
#         # sv_len=str(bk[1])
#         end = str(bk[0] + bk[1])
#         fout.write('DUP' + '\t' + start + '\t' + end)
#         for qname in bk[2]:
#             fout.write('\t' + qname)
#         fout.write('\n')
# with open(work_dir + 'INV.txt', 'w') as fout:
#     for bk in cdup:
#         start = str(bk[0])
#         end = str(bk[0] + bk[1])
#         # sv_len=str(bk[1])
#         fout.write('INV' + '\t' + start + '\t' + end)
#         for qname in bk[2]:
#             fout.write('\t' + qname)
#         fout.write('\n')
#
# with open(work_dir + 'tumor.txt', 'w') as fout:
#     for bk in cdel:
#         start = str(bk[0])
#         end = str(bk[0] + bk[1])
#         fout.write(start + '\t' + end + '\t' + 'DEL' + '\n')
#     for bk in cins:
#         start = str(bk[0])
#         end = str(bk[0] + 1)
#         fout.write(start + '\t' + end + '\t' + 'INS' + '\n')
#     for bk in cinv:
#         start = str(bk[0])
#         end = str(bk[0] + bk[1])
#         fout.write(start + '\t' + end + '\t' + 'INV' + '\n')
#     for bk in cdup:
#         start = str(bk[0])
#         end = str(bk[0] + bk[1])
#         fout.write(start + '\t' + end + '\t' + 'DUP' + '\n')


# def sample(bk1,bk2,seq_list,direction_list,depth_list,basequal_list,mapq_list):
#
#
#     # if bk2-5<bk1+5:
#     #     sv_pos=range(bk1,bk2)
#     # else:
#     if bk1+20>bk2-20:
#         sv_pos=range(bk1,bk2)
#     else:
#         sv_pos=range(bk1+20,bk2-20)
#
#     # print(bk1+20,bk2-20)
#     replace_pos=np.random.choice(sv_pos,size=400,replace=True)
#
#     for i in range(len(seq_list)):
#
#         replace_seq=""
#         replace_direction=""
#         replace_depth=""
#         replace_basequal=list()
#         replace_mapq=list()
#
#         seq=seq_list[i]
#         direction=direction_list[i]
#         depth=depth_list[i]
#         basequal=basequal_list[i]
#         mapq=mapq_list[i]
#
#         for pos in replace_pos:
#             replace_seq=replace_seq+seq[pos]
#             replace_direction=replace_direction+direction[pos]
#             replace_depth=replace_depth+depth[pos]
#             replace_basequal.append(basequal[pos])
#             replace_mapq.append(mapq[pos])
#
#         seq_list[i]=seq[0:bk1]+replace_seq+seq[bk2:]
#         direction_list[i]=direction[0:bk1]+replace_direction+direction[bk2:]
#         depth_list[i]=depth[0:bk1]+replace_depth+depth[bk2:]
#         basequal_list[i]=basequal[0:bk1]+replace_basequal+basequal[bk2:]
#         mapq_list[i]=mapq[0:bk1]+replace_mapq+mapq[bk2:]
#
#     return seq_list,direction_list,depth_list,basequal_list,mapq_list


# somatic_seq_list,somatic_direction_list,\
# somatic_depth_list,somatic_basequal_list,somatic_mapq_list= sample(bk1_in_revised,bk2_in_revised,
#                                                  somatic_seq_list,
#                                                  somatic_direction_list,
#                                                  somatic_depth_list,
#                                                  somatic_basequal_list,)
#
#
# germline_seq_list, germline_direction_list, \
# germline_depth_list,germline_basequal_list ,germline_mapq_list= sample(bk1_in_revised, bk2_in_revised,
#                                                     germline_seq_list,
#                                                     germline_direction_list,
#                                                     germline_depth_list,
#                                                     germline_basequal_list,)


# k=31
# kmer_set=set()
#
# tumor_reads_name=set()
#
# for aln in tumor_sv_reads:
#     tumor_reads_name.add(aln.query_name)

# 以tumor_bam中正常的reads，normal_bam中的reads作为背景板
# tumor_bam=pysam.AlignmentFile(tumor_bam_file,'r')
# tumor_region_reads=tumor_bam.fetch(contig=chro,start=bk1-1000,end=bk2+1000)
#
# for aln in tumor_region_reads:
#     if aln.is_unmapped or aln.mapping_quality < 20:
#         continue
#     else:
#         if aln.query_name not in tumor_reads_name:
#             seq = aln.query_sequence
#             for i in range(0, len(seq) - k + 1):
#                 kmer = seq[i:i + k]
#                 kmer_set.add(kmer)
# tumor_bam.close()
# normal_bam = pysam.AlignmentFile(normal_bam_file, 'r')
# normal_region_reads = normal_bam.fetch(contig=chro, start=bk1 - 1000, end=bk2 + 1000)
# for aln in normal_region_reads:
#     if aln.is_unmapped or aln.mapping_quality < 20:
#         continue
#     else:
#         seq = aln.query_sequence
#         for i in range(0, len(seq) - k + 1):
#             kmer = seq[i:i + k]
#             kmer_set.add(kmer)
# normal_bam.close()

# 遍历ts的sequence，挑选出不在kmer_set里的kmer

# somatic_kmer=set()
# somatic_sum=0
#
# pos=list()
# for aln in tumor_sv_reads:
#     seq=aln.query_sequence
#     pos.append(list())
#     for i in range(0,len(seq)-k+1):
#         kmer=seq[i:i+k]
#         if kmer not in kmer_set:
#             pos[-1].append(i)
#             somatic_sum=somatic_sum+1
#             somatic_kmer.add(kmer)


# 画一下image，对于del和ins，画0 ,1 通道； 对于inv： 画2,3 通道； 对于dup：画 4,5 通道
# dim1=50
# # dim2=500
# dim2=bk2_in_revised-bk1_in_revised+600
# dim2=min(dim2,len(somatic_seq_list[i]))
# somatic_img=Image.new("RGB",(dim2,dim1))    # （宽，高）
# somatic_base_channel=features[0]
# # print("Generate Somatic Image:\tH:",dim1,"\tW:",dim2)
# for i in range(dim1):
#     for j in range(dim2):
#         color=somatic_base_channel[i][j]
#         # print(color,end=" ")
#         somatic_img.putpixel((j,i),(color,0,0))
#     # print(" ")
# somatic_img=np.array(somatic_img)
# print(somatic_img.shape)
# transformed=transform.resize(somatic_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed=Image.fromarray(transformed)
# transformed.save(sv_str+'/somatic_R.png')
#
# germline_img=Image.new("RGB",(dim2,dim1))    # （宽，高）
# germline_base_channel = features[1]
# # print("Generate Somatic Image:\tH:",dim1,"\tW:",dim2)
# for i in range(50):
#     for j in range(dim2):
#         color=germline_base_channel[i][j]
#         # img.putpixel((j,i),(0,0,color))
#         germline_img.putpixel((j, i), (color,0, 0))
#
# germline_img = np.array(germline_img)
# transformed=transform.resize(germline_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed = Image.fromarray(transformed)
# transformed.save(sv_str+'/germline_R.png')
#
# somatic_img = Image.new("RGB", (dim2, dim1))  # （宽，高）
# somatic_base_channel = features[2]
# # print("Generate Somatic Image:\tH:", dim1, "\tW:", dim2)
# for i in range(50):
#     for j in range(dim2):
#         color = somatic_base_channel[i][j]
#         # print(color,end=" ")
#         somatic_img.putpixel((j, i), (0, color, 0))
#     # print(" ")
# somatic_img = np.array(somatic_img)
# transformed=transform.resize(somatic_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed = Image.fromarray(transformed)
# transformed.save(sv_str + '/somatic_G.png')
#
# germline_img = Image.new("RGB", (dim2, dim1))  # （宽，高）
# germline_base_channel = features[3]
# # print("Generate Somatic Image:\tH:", dim1, "\tW:", dim2)
# for i in range(50):
#     for j in range(dim2):
#         color = germline_base_channel[i][j]
#         # img.putpixel((j,i),(0,0,color))
#         germline_img.putpixel((j, i), (0, color, 0))
#
# germline_img = np.array(germline_img)
# transformed=transform.resize(germline_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed = Image.fromarray(transformed)
# transformed.save(sv_str + '/germline_G.png')
#
# somatic_img = Image.new("RGB", (dim2, dim1))  # （宽，高）
# somatic_base_channel = features[4]
# # print("Generate Somatic Image:\tH:", dim1, "\tW:", dim2)
# for i in range(50):
#     for j in range(dim2):
#         color = somatic_base_channel[i][j]
#         # print(color,end=" ")
#         somatic_img.putpixel((j, i), (0, 0, color))
#     # print(" ")
#
# somatic_img = np.array(somatic_img)
# transformed=transform.resize(somatic_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed = Image.fromarray(transformed)
# transformed.save(sv_str + '/somatic_B.png')
#
# germline_img = Image.new("RGB", (dim2, dim1))  # （宽，高）
# germline_base_channel = features[5]
# # print("Generate Somatic Image:\tH:", dim1, "\tW:", dim2)
# for i in range(50):
#     for j in range(dim2):
#         color = germline_base_channel[i][j]
#         # img.putpixel((j,i),(0,0,color))
#         germline_img.putpixel((j, i), (0, 0, color))
# germline_img = np.array(germline_img)
# transformed=transform.resize(germline_img,(50,500))
# transformed=transformed*255
# transformed=transformed.astype(np.uint8)
# transformed = Image.fromarray(transformed)
# transformed.save(sv_str + '/germline_B.png')


# chro=bk[0][0]
# bk1=bk[0][1]
# bk2=bk[0][2]
# sv_type=bk[0][3]
# sv_region_reads=bam.fetch(contig=chro,start=bk1-100,end=bk2+100)
#
# support_reads=list()
# to_merge=list()
# for aln in sv_region_reads:
#     if aln.is_unmapped:
#         continue
#     if sv_type=='DEL' or sv_type=='INS':
#         if aln.has_tag('SA') and ( abs(aln.reference_start-bk[0][1])<=100 or abs(aln.reference_start-bk[0][2])<=100
#                                   or abs(aln.reference_end-bk[0][1])<=100 or abs(aln.reference_end-bk[0][2])<=100):
#             if sv_type=='DEL':
#                 support_reads.append(aln)
#             elif sv_type=='INS':
#                 to_merge.append(aln)
#
#         elif has_long_ID(aln,bk):
#             support_reads.append(aln)
#
#     elif sv_type== 'INV' or sv_type=='DUP':
#         if aln.has_tag('SA') and ( abs(aln.reference_start-bk[0][1])<=50 or abs(aln.reference_start-bk[0][2])<=50
#                                   or abs(aln.reference_end-bk[0][1])<=50 or abs(aln.reference_end-bk[0][2])<=50):
#             support_reads.append(aln)
# if sv_type=='INS':
#     merged=merge_insertion(to_merge)
#     support_reads.extend(merged)
# return support_reads

# start=bk[0]
# end=bk[0]+bk[1]
# if sv_type=="INS":
#     end=start+1
# sv_region_reads = bam.fetch(contig=chro, start=start - 50, end=end + 50)
# support_reads=list()
# for aln in sv_region_reads:
#     if aln.is_unmapped or aln.mapping_quality<20:
#         continue
#     if aln.reference_start<start-50 and aln.reference_end>end+50 and not has_long_ID(aln,start):
#         support_reads.append(aln)
# return support_reads


# insertion_pos = bk[0]
# sa = dict()
# merged = list()
# no_need = list()
#
# to_merge_dict = dict()
#
# for aln in to_merge:
#     if aln.query_name in sa.keys():
#         sa[aln.query_name].append(aln)
#     else:
#         sa[aln.query_name] = [aln]

# for key in sa.keys():
#     for aln in sa[key]:
#         print(aln.query_name,aln.reference_start,aln.reference_end,aln.query_alignment_start,aln.query_alignment_end)


# 找出支持insertion的alignment
# for key in sa.keys():
#     if len(sa[key]) == 1:
#         no_need.append(sa[key][0])
#     else:
#         for aln in sa[key]:
#             if abs(aln.reference_start - insertion_pos) <= 100 or abs(aln.reference_end - insertion_pos) <= 100:
#                 if aln.query_name in to_merge_dict.keys():
#                     to_merge_dict[aln.query_name].append(aln)
#                 else:
#                     to_merge_dict[aln.query_name] = [aln]
#             else:
#                 no_need.append(aln)
# # 只需要处理to_merge就好了
# keys = list(to_merge_dict.keys())
# for k in keys:
#     # 只保留split alignment
#     if len(to_merge_dict[k]) == 2 and to_merge_dict[k][0].is_reverse == to_merge_dict[k][1].is_reverse:
#         if to_merge_dict[k][0].reference_start > to_merge_dict[k][1].reference_start:  # 交换次序，小的在前
#             tmp = to_merge_dict[k][1]
#             to_merge_dict[k][1] = to_merge_dict[k][0]
#             to_merge_dict[k][0] = tmp
#             if to_merge_dict[k][0].cigartuples[-1][1] != 4 or to_merge_dict[k][1].cigartuples[0][1] != 4:
#                 del to_merge_dict[k]
#     else:
#         del to_merge_dict[k]