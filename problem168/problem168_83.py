a,b=map(int,input().split())
List = list(map(int, input().split()))
wa = 0
for i in range(b):
  wa += List[i]
res = a - wa
if res < 0:
  res = -1
print(res)