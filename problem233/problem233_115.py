N = int(input())
P = list(map(int,input().split()))

min_num = float('inf')
ans = 0
for i in P:
  if i < min_num:
    ans+=1
    min_num = i
print(ans)