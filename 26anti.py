# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
rc = ''
for i in range(len(dna)):
	nt = dna[i]
	if     nt == 'A': rc = 'T' + rc
	elif   nt == 'C': rc = 'G' + rc
	elif   nt == 'T': rc = 'A' + rc
	else:  rc = 'C' + rc
print(rc)


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
