n=int(input())
a=list(map(int,input().split()))
temp=sum(a)
ans=0
t=9999999999999999
tsum=0
ta=0
for i in range(n):
  tsum=tsum+a[i]
  if abs(tsum-temp/2)<t:
    t=abs(tsum-temp/2)
    ta=tsum
print(abs(int(ta)*2-temp))