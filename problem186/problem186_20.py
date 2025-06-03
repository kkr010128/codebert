k,n=map(int,input().split())
l =list(map(int, input().split()))
a = []
a.append(l[n-1]- l[0])
for i in range(n-1):
    a.append(k-l[i+1]+l[i])
print(min(a))