N = int(input())
st = [tuple(input().split()) for _ in range(N)]
X = input()

ans = 0
for s, t in st:
    ans += int(t)
for s, t in st:
    ans -= int(t)
    if s == X: break
print(ans)