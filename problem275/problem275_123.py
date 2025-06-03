x,y = map(int,input().split())
if x > 3:
    x = 4
if y > 3:
    y = 4
ans = 0
if x == y == 1:
    ans += 400000
ans += (8-x-y)*100000
print(ans)