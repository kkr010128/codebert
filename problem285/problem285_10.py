s = input()
N = len(s)+1
res = []
ans = 0
i = 0
while i < N-1:
    seq = 1
    while i < N - 2 and s[i] == s[i + 1]:
        i += 1
        seq += 1
    res.append(seq)
    i += 1

if s[0] == '>':
    ans += res[0] * (res[0] + 1) // 2
    res = res[1:]
if s[-1] == '<':
    ans += res[-1] * (res[-1]+1)//2
    res = res[:-1]

for i in range(len(res) // 2):
    tmp = max(res[2 * i], res[2 * i + 1])
    tmp2 = min(res[2 * i], res[2 * i + 1])
    ans += tmp * (tmp + 1) // 2
    ans += tmp2 * (tmp2-1) //2
print(ans)