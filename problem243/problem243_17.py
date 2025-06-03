N = int(input())
tracks = [tuple(input().split()) for _ in range(N)]
X = input()
sleep = False
ans = 0
for s, t in tracks:
    t = int(t)
    if sleep:
        ans += t
    if s == X:
        sleep = True
print(ans)