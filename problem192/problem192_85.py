n = int(input())
a = list(map(int, input().split()))

ns = [0] * (n + 1)
for i in a:
    ns[i] += 1
ans = 0
for i in ns:
    if i > 1:
        ans += i * (i - 1) // 2
for i in a:
    print(min(ans - (ns[i] - 1), ans))
