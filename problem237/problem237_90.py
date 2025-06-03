import sys
input = sys.stdin.readline
N=int(input())
list=[0 for i in range(N)]
for  i in range(N):
 x,l=map(int,input().split())
 list[i]=[x-l,x+l]
list.sort(key=lambda x: x[1])
ans=0
haji=-(10**10)
for  i in range(N):
 if list[i][0]>=haji:
  ans+=1
  haji=list[i][1]
print(ans)
