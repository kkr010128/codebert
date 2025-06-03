import itertools

n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]


cnt=0
num=0
for v in itertools.permutations(xy):
  num+=1
  for i in range(n-1):
    a=(v[i][0]-v[i+1][0])**2+(v[i][1]-v[i+1][1])**2
    b=a**0.5
    cnt+=b

print(cnt/num)