import sys
import argparse
import logging
import time
import re
callset = {1: "cuteSV", 2: "Sniflles", 3: "PBSV", 4: "SVIM",5: "CNNSSV",6:"nanomonsv"}

USAGE="""\
	Evaluate SV callset on NA19240 dataset
"""
def getKV(str):
    ret=dict()
    splits=re.split(';',str)
    for kv in splits:
        infos=re.split('=',kv)
        if len(infos)==2:
            key=re.split('=',kv)[0]
            value=re.split('=',kv)[1]
            ret[key]=value
    return ret
def parseArgs(argv):
	parser = argparse.ArgumentParser(prog="NA19240_eval", description=USAGE, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("base", type=str, help="Base vcf file of NA19240.")
	parser.add_argument("cuteSV", type=str, help="CuteSV vcf file of NA19240.")
	parser.add_argument("CNNSSV", type=str, help="CNNSSV vcf file of NA19240.")
	parser.add_argument("sniffles", type=str, help="Sniffles vcf file of NA19240.")
	parser.add_argument("nanomonsv", type=str, help="nanomonsv vcf file of NA19240.")
	# parser.add_argument("pbsv", type=str, help="PBSV vcf file of NA19240.")
	# parser.add_argument("svim", type=str, help="SVIM vcf file of NA19240.")
	parser.add_argument('-b', '--bias', help = "Bias of overlaping.[%(default)s]", default = 0.7, type = float)
	parser.add_argument('-o', '--offect', help = "Offect of breakpoint distance.[%(default)s]", default = 1000, type = int)
	args = parser.parse_args(argv)
	return args

def pase_base_info(seq):
	info = {'SVLEN': 0, 'END': 0, "SVTYPE": '', "RE": 0}
	for i in seq.split(';'):
		if i.split('=')[0] in ["SVLEN", "END", "RE"]:
			try:
				info[i.split('=')[0]] = abs(int(i.split('=')[1]))
			except:
				pass
		if i.split('=')[0] == "SVTYPE":
			info[i.split('=')[0]] = i.split('=')[1][0:3]
	return info

def load_base_bed(base_path):
	base_call=dict()
	file=open(base_path,'r')
	for line in file:
		seq = line.strip('\n').split("\t")

		chr=seq[0]
		pos=seq[1]
		ALT=seq[3]
		end=seq[2]
		sv_len=seq[4]
		if ALT not in ["INS", "INV", "DEL", "DUP"]:
			continue
		if ALT not in base_call:
			base_call[ALT] = dict()
		if chr not in base_call[ALT]:
			base_call[ALT][chr] = list()
		if ALT == "INV":
			base_call[ALT][chr].append([pos, end - pos + 1, end, 0])
		else:
			if sv_len >= 50 and sv_len <= 100000:
				base_call[ALT][chr].append([pos, sv_len, end, 0])
	file.close()
	return base_call



def load_base(base_path):
	base_call = dict()
	file = open(base_path, 'r')
	for line in file:
		seq = line.strip('\n').split("\t")
		if seq[0][0] == '#':
			continue

		chr = seq[0]
		pos = int(seq[1])
		ALT = seq[4][1:4]
		if ALT not in ["INS", "INV", "DEL", "DUP"]:
			continue
		# if ALT == "DUP":
		# 	ALT = "INS"
		info = pase_base_info(seq[7])
		if ALT not in base_call:
			base_call[ALT] = dict()

		if chr not in base_call[ALT]:
			base_call[ALT][chr] = list()
		if ALT == "INV":
			base_call[ALT][chr].append([pos, info["END"] - pos + 1, info["END"], 0])
		else:
			if info["SVLEN"] >= 50 and info["SVLEN"] <= 100000:
				base_call[ALT][chr].append([pos, info["SVLEN"], info["END"], 0])
	file.close()
	return base_call


def load_CNNSSV(CNNSSV_path):

	CNNSSV_call=dict()
	CNNSSV_call["DEL"] = dict()
	CNNSSV_call["INV"] = dict()
	CNNSSV_call["INS"] = dict()
	CNNSSV_call["DUP"] = dict()
	file=open(CNNSSV_path,'r')
	for line in file:
		seq=line.strip('\n').split('\t')
		if seq[0][0]=='#':
			continue
		chr=seq[0]
		pos=int(seq[1])
		end=int(seq[2])
		ALT=seq[3]
		svlen=int(seq[4])
		if chr not in CNNSSV_call[ALT]:
			CNNSSV_call[ALT][chr]=list()

		# svlen=end-pos
		# if svlen>=50 and svlen<=100000:
		CNNSSV_call[ALT][chr].append([pos,svlen,end,0])
	return CNNSSV_call
def load_nanomonsv(nanomonsv_path):

	nanomonsv_call=dict()
	nanomonsv_call["DEL"] = dict()
	nanomonsv_call["INV"] = dict()
	nanomonsv_call["INS"] = dict()
	nanomonsv_call["DUP"] = dict()
	file=open(nanomonsv_path,'r')
	for line in file:
		infos = re.split('\s+', line)
		if line[0][0]=='#':
			continue
		chr=infos[0]
		pos=int(infos[1])
		ALT=infos[4][1:4]
		if ALT=='DEL' or ALT=='INV' or ALT=='INS' or ALT=='DUP':
			#提取出变异的长度
			# sups = infos[7]
			# sv_len_pos = sups.find(';SVLEN')
			# sv_len_pair = ""
			# for k in range(sv_len_pos + 1, len(sups)):
			# 	if sups[k] != ';' and sups[k]!=' ':
			# 		sv_len_pair = sv_len_pair + sups[k]
			# 	else:
			# 		break
			# sv_len = abs(int(sv_len_pair.split('=')[1]))
			# # 提取出变异的终点
			# sups = infos[7]
			# sv_end_pos = sups.find('END')
			# sv_end_pair = ""
			# for k in range(sv_end_pos + 1, len(sups)):
			# 	if sups[k] != ';' and sups[k]!=' ':
			# 		sv_end_pair = sv_end_pair + sups[k]
			# 	else:
			# 		break
			# sv_end = abs(int(sv_end_pair.split('=')[1]))
			infos=getKV(infos[7])
			if 'SVLEN' in infos.keys():
				sv_len = abs(int(infos['SVLEN']))
			else:
				continue
			if 'END' in infos.keys():
				sv_end=abs(int(infos['END']))
			else:
				continue
			if chr not in nanomonsv_call[ALT]:
				nanomonsv_call[ALT][chr]=list()
			if sv_len>=50 and sv_len<=100000:
				nanomonsv_call[ALT][chr].append([pos,sv_len,sv_end,0])

	return nanomonsv_call
def load_cuteSV(cuteSV_path):
	# inv_tag = 0
	last_inv = list()
	cuteSV_call = dict()
	file = open(cuteSV_path, 'r')
	for line in file:
		seq = line.strip('\n').split("\t")
		if seq[0][0] == '#':
			continue

		chr = seq[0]
		pos = int(seq[1])
		ALT = seq[2][7:10]
		# if ALT == "DUP":
		# 	ALT = "INS"
		if ALT not in ["INS", "INV", "DEL", "DUP"]:
			continue

		info = pase_base_info(seq[7])
		if ALT not in cuteSV_call:
			cuteSV_call[ALT] = dict()

		if chr not in cuteSV_call[ALT]:
			cuteSV_call[ALT][chr] = list()

		if info["SVLEN"] >= 50 and info["SVLEN"] <= 100000:
			if ALT == "INV":
				last_inv.append([ALT, chr, pos, info["SVLEN"], info["END"], info["RE"]])
				# if inv_tag == 0
			else:
				cuteSV_call[ALT][chr].append([pos, info["SVLEN"], info["END"], 0])
				# inv_tag = 0
				if len(last_inv):
					last_inv = sorted(last_inv, key = lambda x:-x[3])
					cuteSV_call[last_inv[0][0]][last_inv[0][1]].append([last_inv[0][2], last_inv[0][3], last_inv[0][4], 0])
					last_inv = list()
	file.close()
	return cuteSV_call

def load_sniffles(sniffles_path):
	sniffles_call = dict()
	last_inv = list()
	file = open(sniffles_path, 'r')
	for line in file:
		seq = line.strip('\n').split("\t")
		if seq[0][0] == '#':
			continue

		chr = seq[0]
		pos = int(seq[1])
		info = pase_base_info(seq[7])

		if info["SVTYPE"] not in ["INS", "INV", "DEL", "DUP"]:
			continue

		# if info["SVTYPE"] == "DUP":
		# 	info["SVTYPE"] = "INS"

		if info["SVTYPE"] not in sniffles_call:
			sniffles_call[info["SVTYPE"]] = dict()

		if chr not in sniffles_call[info["SVTYPE"]]:
			sniffles_call[info["SVTYPE"]][chr] = list()

		if info["SVLEN"] >= 50 and info["SVLEN"] <= 100000:
			if info["SVTYPE"] == "INV":
				last_inv.append([info["SVTYPE"], chr, pos, info["SVLEN"], info["END"], info["RE"]])
			else:
				sniffles_call[info["SVTYPE"]][chr].append([pos, info["SVLEN"], info["END"], 0])
				if len(last_inv):
					last_inv = sorted(last_inv, key = lambda x:-x[3])
					sniffles_call[last_inv[0][0]][last_inv[0][1]].append([last_inv[0][2], last_inv[0][3], last_inv[0][4], 0])
					last_inv = list()

	file.close()
	return sniffles_call

def load_pbsv(pbsv_path):
	pbsv_call = dict()
	file = open(pbsv_path, 'r')
	for line in file:
		seq = line.strip('\n').split("\t")
		if seq[0][0] == '#':
			continue

		chr = seq[0]
		pos = int(seq[1])

		info = pase_base_info(seq[7])

		if info["SVTYPE"] not in ["INS", "INV", "DEL", "DUP"]:
			continue

		# if info["SVTYPE"] == "DUP":
		# 	info["SVTYPE"] = "INS"

		if info["SVTYPE"] not in pbsv_call:
			pbsv_call[info["SVTYPE"]] = dict()

		if chr not in pbsv_call[info["SVTYPE"]]:
			pbsv_call[info["SVTYPE"]][chr] = list()

		if info["SVTYPE"] == "INV":
			pbsv_call[info["SVTYPE"]][chr].append([pos, info["END"] - pos + 1, info["END"], 0])
		else:
			if info["SVLEN"] >= 50 and info["SVLEN"] <= 100000:
				pbsv_call[info["SVTYPE"]][chr].append([pos, info["SVLEN"], info["END"], 0])
	file.close()
	return pbsv_call

def load_svim(base_path):
	base_call = dict()
	file = open(base_path, 'r')
	for line in file:
		seq = line.strip('\n').split("\t")
		if seq[0][0] == '#':
			continue

		chr = seq[0]
		pos = int(seq[1])
		ALT = seq[4][1:4]
		if ALT not in ["INS", "INV", "DEL", "DUP"]:
			continue
		# if ALT == "DUP":
		# 	ALT = "INS"
		info = pase_base_info(seq[7])
		if ALT not in base_call:
			base_call[ALT] = dict()

		if chr not in base_call[ALT]:
			base_call[ALT][chr] = list()

		if ALT == "INV":
			base_call[ALT][chr].append([pos, info["END"] - pos + 1, info["END"], 0])
		else:
			if info["SVLEN"] >= 50 and info["SVLEN"] <= 100000:
				base_call[ALT][chr].append([pos, info["SVLEN"], info["END"], 0])
	file.close()
	return base_call

def cmp_callsets(base, call, flag, Bias, Offect):

	# kv=open('/home/duan/Desktop/CNNSSV.somatic7.kv',"w")
	# fn=open('/home/duan/Desktop/CNNSSV.somatic7.fn',"w")
	for svtype in base:
		if svtype not in call:
			continue
		else:
			for chr in base[svtype]:
				if chr not in call[svtype]:
					continue
				else:
					for i in base[svtype][chr]:
						for j in call[svtype][chr]:
							if i[0] - Offect <= j[0] <= i[2] + Offect or i[0] - Offect <= j[2] <= i[2] + Offect or j[0] - Offect <= i[0] <= j[2] + Offect:
								if min(i[1], j[1])*1.0/max(i[1], j[1]) >= Bias:
									# kv.write(chr + '\t' + str(i[0]) + '\t' + str(i[2]) + '\t' + svtype + '\t' + str(i[1]) + '\n')
									# kv.write(chr + '\t' + str(j[0]) + '\t' + str(j[2]) + '\t' + svtype + '\t' + str(j[1]) + '\n')
									i[3] = flag
									j[3] = flag
								else:
									pass
	total_base = 0
	tp_base = 0
	# for svtype in ["INS"]:
	# for svtype in ["DUP"]:
	# for svtype in ["DEL"]:
	# for svtype in ["INS", "DEL"]:
	# for svtype in ["INS", "DEL", "INV"]:
	for svtype in ["INS", "DEL", "INV", "DUP"]:
	# for svtype in ["INV"]:
	# 	if svtype in base.keys():
		for chr in base[svtype]:
			for i in base[svtype][chr]:
				total_base += 1
				if i[3] == flag:
					# tb.write(chr + '\t' + str(i[0]) + '\t' + str(i[2]) + '\t' + svtype + '\t' + str(i[1]) + '\n')
					tp_base += 1
				# else:
				# 	fn.write(chr + '\t' + str(i[0]) + '\t' + str(i[2]) + '\t' + svtype + '\t' + str(i[1]) + '\n')
			# else:
			# 	print(flag, svtype, chr, i[0], i[1], i[2])
# logging.info("Base count: %d"%(total_base))
	# logging.info("TP-base count: %d"%(tp_base))
	logging.info("====%s===="%(callset[flag]))
	total_call = 0
	tp_call = 0
	# for svtype in ["INS"]:
	# for svtype in ["DUP"]:
	# for svtype in ["DEL"]:
	# for svtype in ["INS", "DEL"]:
	# for svtype in ["INS", "DEL", "INV"]:

	# fout=open('/Users/duan/Desktop/somatic_tp.bed','w')

	for svtype in ["INS", "DEL", "INV", "DUP"]:
	# for svtype in ["INV"]:
	# 	if svtype in call.keys():
		for chr in call[svtype]:
			for i in call[svtype][chr]:
				total_call += 1
				if i[3] == flag:
					tp_call += 1
					# print(i)
					# tp.write(chr+'\t'+str(i[0])+'\t'+str(i[2])+'\t'+svtype+'\t'+str(i[1])+'\n')
				# else:
				# 	fp.write(chr+'\t'+str(i[0])+'\t'+str(i[2])+'\t'+svtype+'\t'+str(i[1])+'\n')

	# fout.close()


	logging.info("Camp count: %d"%(total_call))
	logging.info("TP-call count: %d"%(tp_call))
	logging.info("Precision: %.2f"%(100.0*tp_call/total_call))
	logging.info("Recall: %.2f"%(100.0*tp_base/total_base))
	logging.info("F-measure: %.2f"%(200.0*tp_base*tp_call/(total_base*tp_call+tp_base*total_call)))

	print(tp_base)
	print(total_base)
	# print(tp_base)
	# print(total_base)
	# tb.close()
	# fp.close()
	# kv.close()
	# fn.close()

def main_ctrl(args):
	# pass
	base_call = load_base(args.base)

	nanomonsv_call=load_nanomonsv(args.nanomonsv)
	cuteSV_call = load_cuteSV(args.cuteSV)
	CNNSSV_call = load_CNNSSV(args.CNNSSV)
	sniffles_call = load_sniffles(args.sniffles)
	# pbsv_call = load_pbsv(args.pbsv)
	# svim_call = load_svim(args.svim)
	# for svtype in sniffles_call:
	# 	for chr in sniffles_call[svtype]:
	# 		for i in sniffles_call[svtype][chr]:
	# 			print(svtype, chr, i)

	cmp_callsets(base_call, cuteSV_call, 1, args.bias, args.offect)
	cmp_callsets(base_call, sniffles_call, 2, args.bias, args.offect)
	# cmp_callsets(base_call, pbsv_call, 3, args.bias, args.offect)
	# cmp_callsets(base_call, svim_call, 4, args.bias, args.offect)
	cmp_callsets(base_call,CNNSSV_call,5,args.bias,args.offect)
	cmp_callsets(base_call,nanomonsv_call,6,args.bias,args.offect)

	

def main(argv):
	args = parseArgs(argv)
	setupLogging(False)
	# print args
	starttime = time.time()
	main_ctrl(args)
	logging.info("Finished in %0.2f seconds."%(time.time() - starttime))

def setupLogging(debug=False):
	logLevel = logging.DEBUG if debug else logging.INFO
	logFormat = "%(asctime)s [%(levelname)s] %(message)s"
	logging.basicConfig( stream=sys.stderr, level=logLevel, format=logFormat )
	logging.info("Running %s" % " ".join(sys.argv))

if __name__ == '__main__':
	main(sys.argv[1:])
