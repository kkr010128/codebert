import sys

INF = 10**60

inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

min_sum = INF

i = 0
j = 0

for k in range(1,n):
    if k > n**0.5:
        break
    if n/k % 1 != 0:
        continue
    i = k
    j = n/k
    if i+j < min_sum:
        min_sum = i+j

print(int(min_sum - 2))
