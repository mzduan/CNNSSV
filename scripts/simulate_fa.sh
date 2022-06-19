#!/bin/bash

VISOR='/home/yelab/dmz/VISOR/'
scripts='/home/yelab/dmz/scripts/'
get_N_region='/home/yelab/dmz/scripts/get_N_region.py'
eliminate_seq='/home/yelab/dmz/scripts/eliminate_random_seq.py'
split_two_parts='/home/yelab/dmz/scripts/split_two_parts.py'

#计算各染色体的维度
#for i in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
#do
#	chr_name=ref/chr$i.fa.fai
#	dim_name=dim/chr$i.dim.tsv
#	cut -f1,2 $chr_name > $dim_name
#done



#计算各染色体N区域
#for i in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
#do
#	python $get_N_region ref/chr$i.fa exclude/chr$i.bed chr$i
#done


#模拟SV
for i in {1,20}
#for i in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
do

	echo "Generate SVs"
	Rscript $VISOR'scripts/randomregion.r' -d dim/chr$i.dim.tsv -n 1000 -l 500 -s 10 -x exclude/chr$i.bed -v 'deletion,inversion,tandem duplication,insertion' -r '25:25:25:25' | sortBed >  sv/chr$i.sv.bed

	echo "Remove random seq"
	python $eliminate_seq sv/chr$i.sv.bed 


	echo "Split into somatic and germline"
	python $split_two_parts sv/chr$i.sv.bed sv/ chr$i


	echo "Generate germline fa(VISOR HACk)"
	VISOR HACk -g ref/chr$i.fa -bed sv/chr$i.germline.bed -o fa/germline_fa_chr$i
	samtools faidx fa/germline_fa_chr$i/h1.fa 
		


	cut -f1,2 fa/germline_fa_chr$i/h1.fa.fai  | sort | awk '$2 > maxvals[$1] {lines[$1]=$0; maxvals[$1]=$2} END { for (tag in lines) print lines[tag] }' | awk 'OFS=FS="\t"''{print $1, "0", $2, "100.0", "100.0"}' > sim/chr$i.germline.bed


	echo "Generate somatic fa(VISOR HACk)"	
	VISOR HACk -g ref/chr$i.fa -bed sv/chr$i.sv.bed -o fa/somatic_fa_chr$i
	samtools faidx fa/somatic_fa_chr$i/h1.fa

	cut -f1,2 fa/somatic_fa_chr$i/h1.fa.fai  | sort | awk '$2 > maxvals[$1] {lines[$1]=$0; maxvals[$1]=$2} END { for (tag in lines) print lines[tag] }' | awk 'OFS=FS="\t"''{print $1, "0", $2, "100.0", "100.0"}' > sim/chr$i.somatic.bed
done

