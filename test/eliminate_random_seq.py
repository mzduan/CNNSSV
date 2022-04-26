import sys
import re
if __name__ == '__main__':
    sv_file_name = sys.argv[1]


    fout=open('filtered_'+sv_file_name,'w')
    with open(sv_file_name,'r') as fin:
        while True:
            l=fin.readline()
            if l:
                infos=re.split('\s+',l)
                if infos[3]=='tandem':
                    infos[6]=='0'
                else:
                    infos[5]=='0'
                fout.write(l)
            else:
                break

    fout.close()
