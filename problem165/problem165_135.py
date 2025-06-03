# C gacha

N = int(input())

goods = set()
cnt = 0
for i in range(N):
  S = input()
  if S not in goods:
    goods.add(S)
    cnt += 1
print(cnt)