n,k = map(int,input().split())
p = map(int,input().split())

a = sorted(p)
print(sum([a[i] for i in range(k)]))
