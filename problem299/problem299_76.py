n=int(input())
s=list(map(int,input().split()))
p=["0"]*n
for i in range(n):
  p[s[i]-1]=str(i+1)
p=' '.join(p)
print(p)