N=int(input())
a=[int(x) for x in input().split()]
cnt=0
for i in range(N):
  if i%2==0 and a[i]%2==1:
    cnt+=1
print(cnt)
