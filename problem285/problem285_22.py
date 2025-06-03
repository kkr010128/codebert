s = input()

cnt = [1] if s[0] == "<" else [0, 1]

bc = s[0]

for i in range(1, len(s)):
    if s[i] == bc:
        cnt[-1] += 1
    else:
        cnt.append(1)
    bc = s[i]

if len(cnt) % 2 == 1:
    cnt.append(0)


ans = 0

for i in range(0, len(cnt), 2):
    ma = max(cnt[i], cnt[i + 1])
    mi = min(cnt[i], cnt[i + 1])
    ans += max(0, ma * (ma + 1) // 2)
    ans += max(0, (mi - 1) * mi // 2)

print(ans)
