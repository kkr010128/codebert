N = int(input())
As = list(map(int, input().split()))
P = 1000000007

lst = [0,0,0]
rlt = 1

for i in range(N):
  cnt = lst.count(As[i])
  rlt *= cnt
  rlt %= P
  for j in range(3):
    if lst[j] == As[i]:
      lst[j] += 1
      break
      
print(rlt)