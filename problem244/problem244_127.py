from sys import stdin

line = stdin.readline()
input = [int(x) for x in line.rstrip().split()]

if input[0] * 500 >= input[1]:
    print('Yes')
else:
    print('No')