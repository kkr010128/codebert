import sys
x, y = map(int, input().split())
ans = 0
for i in range(x+1):
    if y == i*2 + (x - i)* 4:
        ans = 1
        break
        
if ans == 1:
    print("Yes")
else:
    print("No")