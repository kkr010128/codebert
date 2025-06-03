N,K = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

sorted_P = sorted(P)

print(sum(sorted_P[:K]))