import sys
input = sys.stdin.readline

x, y = [int(x) for x in input().split()]
ans = 0

for i in [x, y]:
    if i == 1:
        ans += 300000
    elif i == 2:
        ans += 200000
    elif i == 3:
        ans += 100000
    
if x == 1 and y == 1:
    ans += 400000

print(ans)

    
