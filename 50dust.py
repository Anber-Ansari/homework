#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import math
import argparse
import mcb185

def entropy(probs):
	assert(math.isclose(1.0, sum(probs)))
	h = 0
	for p in probs:
		if p != 0: h -= p * math.log2(p)
	return h

def seqentropy(seq):
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	T = seq.count('T')/len(seq)
	G = seq.count('G')/len(seq)
	return entropy([A, C, T, G])

parser = argparse.ArgumentParser(description = '50dust')

parser.add_argument('file', type = str, metavar = '<path>', help = 'mcb185')

parser.add_argument('-w', '--win', required = False, type = int, default = 11,
	metavar = '<int>', help = 'optional integer argument [%(default)i]')

parser.add_argument('-t', required = False, type = float, default = 1.4,
	metavar = '<float>', help = 'optional floating point argument [%(default).1f]')

parser.add_argument('-n', action = 'store_true', help = 'mask with N')

parser.add_argument('--wrap', required = False, type = int, default = 60, 
	metavar = '<int>', help = 'wrapping [%(default)i]')
	
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	seqq = list(seq)
	for i in range(len(seq) -arg.win +1):
		win = seq[i:i+arg.win]
		if seqentropy(win) < arg.t:
			for j in range(i, i+arg.win):
				if arg.n:
					seqq[j] = 'N'
				else: seqq[j] = seq[j].lower()
	seq = ''.join(seqq)
	print(f'>{defline}')
	for i in range(0, len(seq), arg.wrap):
		print(seq[i:i+arg.wrap])
		
 
	

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
