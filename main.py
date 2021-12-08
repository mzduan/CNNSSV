import argparse
from breakpoints import get_breakpoints
from features import run
# from SiameseTest import predict
from test import predict
import sys
import os
import time
import reference
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--tumor", help="tumor bam", type=str,required=True)
    parser.add_argument("--normal", help="normal bam", type=str,required=True)
    parser.add_argument("--ref", help="reference fasta", type=str,required=True)
    parser.add_argument("--model", help="trained cnn model", type=str,required=True)
    parser.add_argument("--wkdir", help="work dir", type=str,required=True)
    parser.add_argument("--output", help="output sv bed", type=str,required=True)
    parser.add_argument("--min_support_read", help="min support read(default=1)", default=1,type=int,required=False)
    parser.add_argument("--min_sv_len", help="min sv len(default=30)", default=30, type=int, required=False)
    parser.add_argument("--max_sv_len", help="min sv len(default=10000)", default=10000, type=int, required=False)
    parser.add_argument("--min_map_qual", help="min map qual(default=20)", default=20, type=int, required=False)
    parser.add_argument("-t", help="thead number", type=int, required=True)
    args = parser.parse_args()

    if os.path.exists(args.wkdir):
        os.system('rm -rf '+args.wkdir)
        os.mkdir(args.wkdir)
    else:
        os.mkdir(args.wkdir)
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()))
    print("Find Candidate SVs")

    ref_dict = reference.initial_fa(args.ref)
    cdel,cins,cinv,cdup=get_breakpoints(args.tumor,args.min_support_read,args.min_sv_len,args.max_sv_len,args.min_map_qual,ref_dict=ref_dict)

    # DEL:   [[pos,len,[read_name_list],[read_start_list],[read_end_list],[ref_start_list],[len_list],mean_left_confu,mean_right_confu]
    # INS:   [[pos,len,[read_name_list],insert_seq,[read_start_list],[read_end_list],[ref_start_list],[len_list],mean_left_confu,mean_right_confu]
    # INV:   [[pos,len,[read_name_list],[read_start_list],[read_end_list],[ref_start_list],[ref_end_list],mean_left_confu,mean_right_confu]
    # DUP:   [[pos,len,[read_name_list],[read_start_list],[read_end_list],[ref_start_list],[ref_end_list],mean_left_confu,mean_right_confu]

    with open(args.wkdir+'/tumor.candidate.bed','w') as fout:
        for key in cdel:
            chro=key
            for bk in cdel[chro]:
                fout.write(chro+'\t'+str(bk[0])+'\t'+str(bk[0]+bk[1])+'\t'+'DEL\t'+str(bk[1])+'\n')
        for key in cins:
            chro=key
            for bk in cins[chro]:
                fout.write(chro+'\t'+str(bk[0])+'\t'+str(bk[0]+1)+'\t'+'INS\t'+str(bk[1])+'\n')
        for key in cinv:
            chro=key
            for bk in cinv[chro]:
                fout.write(chro + '\t' + str(bk[0]) + '\t' + str(bk[0] + bk[1]) + '\t' + 'INV\t'+str(bk[1])+'\n')
        for key in cdup:
            chro=key
            for bk in cdup[chro]:
                fout.write(chro + '\t' + str(bk[0]) + '\t' + str(bk[0] + bk[1]) + '\t' + 'DUP\t'+str(bk[1])+'\n')
    print("Generate Features for Cancidate SVs")
    run(cdel,cins,cinv,cdup,ref_dict,args.tumor,args.normal,args.wkdir,int(args.t))
    # print("Predict...")
    # predict(args.model,args.wkdir,args.output)
    # print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()))
    #

