import sys

"""
Script that counts the number of lines in a file.
Receives a file name as an argument.
"""

fname = sys.argv[1]

f = open(fname, 'r')
count = 0

for line in f:
    count += 1

print(count)