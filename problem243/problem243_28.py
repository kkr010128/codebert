N = int(input())
set_list = [input().split() for _ in range(N)]
X = input()
ans = 0
flg = False

for i in range(N):
  if flg == True:
    ans += int(set_list[i][1])
  if set_list[i][0] == X:
    flg = True
    
print(ans)