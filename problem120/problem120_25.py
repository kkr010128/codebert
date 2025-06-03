N, K = [int(v) for v in input().split()]
P = [int(v) for v in input().split()]

print(sum(sorted(P)[:K]))