N=int(input())
p=[list(map(str,input().split())) for _ in range(N)]
X=input()
flag=0
cnt=0
for i in range(N):
 if flag==1:
  cnt=cnt+int(p[i][1])
 if p[i][0]==X:
  flag=1
print(cnt)