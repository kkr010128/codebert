n=int(input())
p=map(int,input().split())
mi = n+1
ans = 0
for i in p:
  if mi > i:
    mi = i
    ans+=1

print(ans)