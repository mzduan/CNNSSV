import multiprocessing
import glob
import os
import re
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
if __name__ == '__main__':
    kv=getKV("DBVARID=nssv14269924;SVTYPE=INS;IMPRECISE;END=142869;CIPOS=0,.;CIEND=.,0;SVLEN=7093;EXPERIMENT=1;SAMPLE=NA19240;REGIONID=nsv3215982");
    for k in kv.keys():
        print(k,kv[k])