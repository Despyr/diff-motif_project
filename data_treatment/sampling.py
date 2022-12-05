from collections import Counter 
from Bio import SeqIO
from random import sample
import sys

args=sys.argv[1:]

with open(args[0]) as f:
	seqs = SeqIO.parse(f, "fasta")
	samps = ((seq.name, seq.seq) for seq in  sample(list(seqs),10))
	for samp in samps:
