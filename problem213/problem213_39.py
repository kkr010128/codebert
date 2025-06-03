N=int(input())
List = list(map(int, input().split()))
res = 1000000000000
mid = 0
for i in range(101):
  for j in range(N):
    mid += (i-List[j])**2
  res = min(res,mid)
  mid = 0
print(res)