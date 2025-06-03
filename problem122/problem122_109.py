import sys
N = int(input())
A = tuple(map(int, input().split()))
count = [0] * (10 ** 5 + 1)

for a in A:
    count[a] += 1
s = sum(A)

Q = int(input())
for _ in range(Q):
    b, c = map(int, sys.stdin.readline().split())
    s -= count[b] * b
    s += count[b] * c
    count[c] += count[b]
    count[b] = 0
    print(s)