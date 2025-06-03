a,b = map(int, input().split())

ans = 0
for i in range(10000):
    x = int(i*0.08)
    y = int(i*0.10)
    if x == a and y == b:
        ans = i
        break
if ans == 0:
    print(-1)
    exit()
print(ans)
