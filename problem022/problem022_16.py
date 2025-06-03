#coding: UTF-8
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
ans = 0
for v in T:
  if v in S:
    ans += 1
print(ans)
