from collections import defaultdict
money = defaultdict(int)
for i, m in enumerate([300000, 200000, 100000]):  
    money[i] = m
    
X, Y = map(int, input().split())
X -= 1; Y -= 1
ans = money[X] + money[Y]
if X + Y:
    print(ans)
else:
    print(ans + 400000)