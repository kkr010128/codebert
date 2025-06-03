n,k = input().split()
k = int(k)
#print(n,k)
p = [int(s) for s in input().split()]
p.sort()
#print(p)
#print(k)
p2 = p[0:k]
#print(p2)
s = sum(p)
#print(s)
print(sum(p2))