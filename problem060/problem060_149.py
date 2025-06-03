import sys

lines = [list(map(int,line.split())) for line in sys.stdin]
n,m,l = lines[0]

A = lines[1:n+1]
B = [i for i in zip(*lines[n+1:])]

for a in A:
    row = []
    for b in B:
        row.append(sum([i*j for i,j in zip(a,b)]))
    print (" ".join(map(str,row)))