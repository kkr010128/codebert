n=int(input())
li = list(map(int,input().split()))
a=0
for i in range(n):
  for j in range(n):
    a += li[i]*li[j]
b=0
for i in range(n):
    b+= li[i]*li[i]
print((a-b)//2)

