# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

GCsum = 0
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'C' or nt == 'G' : 
		GCsum += 1
GCper = GCsum / len(dna)
print(f'{GCper:.2f}')
		
	
	


"""
python3 24gc.py
0.42
"""
