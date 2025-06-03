n=int(input())
s=list(map(int,input().split()))
p=[0]*n
for i in range(n):
  p[s[i]-1]=i+1
print(*p)