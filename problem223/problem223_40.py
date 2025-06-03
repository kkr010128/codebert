n, k = map(int, input().split())
p = list(map(lambda x: int(x) + 1, input().split()))

s = 0
e = k
t = sum(p[0:k])

ans = 0
while True:
    ans = max(ans, t)
    if e == n:
        break
    t -= p[s]
    t += p[e]
    s += 1
    e += 1

print(ans / 2)
