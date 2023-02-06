# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library
psum = 0
n = 5
factorial = 1
for i in range(1, n+1):
	psum += i
	factorial *= i
print(n, psum, factorial)

"""
python3 22sumfac.py
5 15 120
"""
