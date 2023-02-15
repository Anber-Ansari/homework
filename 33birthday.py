# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import random
import sys

days = int(sys.argv[1])
people = int(sys.argv[2])
precision = 100
shared = 0

for i in range(precision):
	found = False
	cal = [0] * days 
#print(cal) check
	for j in range(people): 
		day = random.randint(1, days -1)
		cal[day] += 1
		for bday in cal: 
			if bday > 1: #more than one is a shared bday
				found = True
				break #stop the loop
	if found:
		shared += 1
print(f'{shared/precision:.3f}')
	
	
"""
python3 33birthday.py 365 23
0.571
"""

