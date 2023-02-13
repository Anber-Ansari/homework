# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

print(sys.argv) #check program

vals = []
valcount = 0
for thing in sys.argv[1:]:
	vals.append(float(thing))
	valcount += 1
average = sum(vals) / valcount
print('Count:', valcount)
print('Minimum:', min(vals))
print('Maximum:', max(vals)) 
print('Mean:', average)

psum = 0
for val in vals:
	psum += (val - average) ** 2
variance = psum / len(vals)
stddev = variance ** 0.5
print('Std. dev:', f'{stddev:.3f}')

vals.sort()
mid = len(vals)
if mid % 2 == 1:
	median = vals[mid//2]
else: 
	median =(vals[mid//2])
	median =(vals[mid//2-1])
print('Median', f'{median:.3f}')





"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
