from Bio import SeqIO
def initial_fa(fa_file):
    records = list(SeqIO.parse(fa_file, "fasta"))
    ref_seq_dict = {}
    for record in records:
        chrom = record.id
        ref_seq_dict[chrom] = record.seq

    return ref_seq_dict

def fetch_ref_seq(opened_ref, chr, start, end):
    ref_cutted = opened_ref.fetch(chr, start, end)
    return ref_cutted