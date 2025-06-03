l,r,d = map(int,input().split())
#print(l,r,d)
ans = 0

for i in range(101):
    if d * i > r:
        break
    elif d * i >= l:
        ans += 1
        continue
    else:
        continue

print(ans)