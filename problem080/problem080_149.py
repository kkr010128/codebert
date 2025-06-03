N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Z = sorted([x+y for x,y in A])
W = sorted([x-y for x,y in A])

print(max(Z[-1]-Z[0], W[-1]-W[0]))