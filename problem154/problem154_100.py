N, K = [int(v) for v in input().split()]

S = [0] * N

for _ in range(K):
    snack = int(input())
    snukes = [int(v) for v in input().split()]
    for snuke in snukes:
        S[snuke-1] = 1

print(sum(x == 0 for x in S))
