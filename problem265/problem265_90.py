n=int(input())
ans=':('
for i in range(1,n+1):
  if int((i*1.08)//1)==n:
    ans=i
    break
print(ans)
