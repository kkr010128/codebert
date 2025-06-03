k, n = map(int, input().split())
a = sorted(list(map(int, input().split())))
x = [(a[i]-a[i-1]) for i in range(1,n)]
x.append(k-a[n-1]+a[0])
y=sorted(x)

print(sum(y[:-1]))        

