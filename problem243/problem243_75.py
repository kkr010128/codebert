n=int(input())
a=[list(input().split()) for _ in range(n)]
x=input()
s=0
for i in range(n):
  if a[i][0]==x:
    p=i
    break
for i in range(p+1,n):
  s+=int(a[i][1])
print(s)