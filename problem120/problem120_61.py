N, K = map(int, input().split())
P = sorted([int(i) for i in input().split()])
print(sum(P[:K]))