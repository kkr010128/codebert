N, K = (int(a) for a in input().split())
p = [int(a) for a in input().split()]

p.sort()
print(sum(p[:K]))