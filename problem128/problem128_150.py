x,n = map(int, input().split())
p = list(map(int, input().split()))
ans = 0

for i in range(x+1):
    if x - i not in p:
        ans = x - i
        break
    elif x + i not in p:
        ans = x + i
        break

print(ans)