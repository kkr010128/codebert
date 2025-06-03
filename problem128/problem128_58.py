X, N = map(int, input().split())
p = list(map(int, input().split()))

for i in range(110):
    if X - i not in p:
        ans = X - i
        break
    elif X + i not in p:
        ans = X + i
        break

print(ans)