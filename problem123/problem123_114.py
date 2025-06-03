b=int(input())
a=list(map(int,input().split()))
ans=""
total=0
for i in a:
  total^=i
for i in a:
  ans+=str(total^i)+" "
print(ans)