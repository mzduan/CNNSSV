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
                    fout.write(infos[0]+'\t'+infos[1]+'\t'+infos[2]+'\t'+"tandem duplication"+'\t'+infos[5]+'\t'+'0'+'\n')

                else:
                    fout.write(infos[0]+'\t'+infos[1]+'\t'+infos[2]+'\t'+infos[3]+'\t'+infos[4]+'\t'+'0'+'\n')
            else:
                break

    fout.close()
