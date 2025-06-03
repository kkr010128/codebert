money = [0, 300000, 200000, 100000]
a,b = map(int, input().split())

st = money[a if a < len(money) else 0] \
 + money[b if b < len(money) else 0]
if a == 1 and b == 1:
  st += 400000
print(st)