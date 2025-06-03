x, y = map(int, input().split())
cnt = 0
for i in range(x+1):
    for j in range(x+1):
        if i + j == x and i*2+j*4 == y:
            cnt += 1
print("Yes") if cnt > 0 else print("No")