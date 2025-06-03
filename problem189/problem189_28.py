ri = lambda S: [int(v) for v in S.split()]
N, M = ri(input())

c = 0
c += (M * (M-1)) / 2
c += (N * (N-1)) / 2

print(int(c))