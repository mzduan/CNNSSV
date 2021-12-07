tumor_kv = open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.tumor7.kv', 'r')
lost_tp = open('/home/duan/Desktop/getBreakpoint/results/mixed/cutesv/cutesv.somatic7.lost_tp.txt', 'r')
gd = open('/home/duan/Desktop/getBreakpoint/groundtruth/NA19239_NA19240/NA19240.chr20.somatic.vcf', 'r')

fout = open('/home/duan/Desktop/getBreakpoint/groundtruth/NA19239_NA19240/NA19240.chr20.somatic.version2.vcf', 'w')

gd_dict = dict()
while True:
    l = gd.readline()
    if l:
        splits = re.split('\s+', l)

        sv_start = int(splits[1])
        gd_dict[sv_start] = l
    else:
        break
gd.close()

kv_dict = dict()
while True:
    l1 = tumor_kv.readline()
    if l1:
        l2 = tumor_kv.readline()
        kv_dict[l2] = l1
    else:
        break
tumor_kv.close()

while True:
    l = lost_tp.readline()
    if l:
        tb = kv_dict[l]
        splits = re.split('\s+', tb)
        tb_pos = int(splits[1])
        if tb_pos in gd_dict.keys():
            gd_dict.pop(tb_pos)
    else:
        break
lost_tp.close()

for k in gd_dict.keys():
    fout.write(gd_dict[k])

fout.close()