x, y = map(int,input().split())

ans = 0

for i in range(x+1):
    for j in range(x+1):
        if 2*i + 4 * j == y and i + j == x:
            ans += 1
            
if ans > 0:
    print('Yes')
else:    
    print('No')