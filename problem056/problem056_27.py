import sys

i,j = input().split()

matrixa = []

for _ in range(int(i)):
    matrixa += [[int(n) for n in sys.stdin.readline().split()]]

matrixb =[ int(num) for num in sys.stdin.readlines() ]

matrixc = [ 0 for _ in range(int(i))]

for n in range(int(i)):
    for a,b in zip(matrixa[n],matrixb):
        matrixc[n] += a*b
for c in matrixc:
    print(c)
