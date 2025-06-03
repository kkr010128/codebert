h = int(input())
ans = 0
m = 1
while True:
    if h == 1 :
        ans += 1
        break
    else:
        h = h//2
        m *= 2
        ans += m
print(ans)
