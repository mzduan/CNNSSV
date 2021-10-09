class SimpleAln:
    def __init__(self,ref_pos,is_rev,cigar,is_sup):
        self.ref_start=ref_pos
        self.direction='-' if is_rev else '+'
        self.cigar=cigar
        self.is_pri=not is_sup