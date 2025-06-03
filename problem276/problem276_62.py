n = int(input())
a = list(map(int, input().split()))
total = sum(a)
s = 0
for bar in a:
    if (s + bar) * 2 <= total:
        s += bar
    else:
        ans = min((s + bar) * 2 - total, total - s * 2)
        break

print(ans)
