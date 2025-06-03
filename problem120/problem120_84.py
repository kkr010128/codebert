n,k = map(int,input().split())
p = [int(x) for x in input().split()]

p.sort()
print(sum(p[0:k]))
