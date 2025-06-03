N = int(input())
S = [input() for _ in range(N)]
S.sort()
check = [True]*N
item = ""
item_ = ""
dict_item = {}
cnt = 0

for i in range(N):
  item_ = S[i]
  if item_ != item:
    item = item_
    cnt += 1
print(cnt)