s = input()[::-1]
l = [0 for i in range(2019)]
l[0] = 1
a, b = 0, 1
ans = 0
for i in s:
    a += int(i) * b
    a %= 2019
    b *= 10
    b %= 2019
    l[a] += 1
for i in l:
    ans += i * (i - 1) // 2
print(ans)