k,n=map(int,input().split())
a = list(map(int,input().split()))
s = []
for i in range(n-1):
  s.append(abs(a[i+1] - a[i]))
s.append(k-a[-1]+a[0])
print(k-max(s))