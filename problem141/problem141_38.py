n = int(input())
a = list(map(int, input().split()))
s = sum(a)
l = [1]
for i in range(n + 1):
    s -= a[i]
    m = min(s, (l[i] - a[i]) * 2)
    if m < 0:
        print(-1)
        exit()
    l.append(m)
print(sum(l))