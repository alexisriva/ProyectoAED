import sys

"""
Script that counts the number of lines in a file.
Receives a file or list of files as argument.
"""

file_count = []

for i in range(1, len(sys.argv)):
    count = 0

    f = open(sys.argv[i], 'r')

    for line in f:
        count += 1

    file_count.append(count)

print(file_count)