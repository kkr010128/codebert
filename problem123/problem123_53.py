n=int(input())
li=list(map(int,input().split()))
ans=0
for i in range(n):
  ans=ans^li[i]
for i in range(n):
  print(ans^li[i],end=" ")
print()


