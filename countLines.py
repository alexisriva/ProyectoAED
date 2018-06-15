import sys

fname = sys.argv[1]

f = open(fname, 'r')
count = 0

for line in f:
    count += 1

print(count)