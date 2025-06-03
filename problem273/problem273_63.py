n, k = map(int, input().split())
a = list(map(int, input().split()))
a2 = [0]
for i in range(n):
    a2.append(a2[-1] + a[i] - 1)
a2 = [a2[i] % k for i in range(n + 1)]
count = {}
temp = a2[:min(k, len(a2))]
for i in temp:
    count.setdefault(i, 0)
    count[i] += 1
ans = 0
for i in count.values():
    ans += (i * (i - 1) // 2)
for i in range(1, len(a2) - len(temp) + 1):
    temp = a2[i: i + len(temp)]
    temp2 = temp[:-1]
    ans += temp2.count(temp[-1])
print(ans)