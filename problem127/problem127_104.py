x,y = map(int, input().split())

ans = 'No'

for i in range(x+1):
    for j in range(y+1):
        if i + j > x:
            continue

        if i*2 + j*4 == y and i+j == x:
            ans = 'Yes'

print(ans)