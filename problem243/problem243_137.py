N = int(input())
X = []
for i in range(N):
  X.append(input().split())
  
S = input()

flg = False
ans = 0
for x in X:
  if flg:
    ans += int(x[1])
  if S == x[0]:
    flg = True
    
print(ans)