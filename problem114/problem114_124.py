D = int(input())
c = list(map(int, input().split()))
s = []
c_sum = sum(c)
for i in range(D):
    tmp = list(map(int, input().split()))
    s.append(tmp)
t = []
for i in range(D):
    tmp = int(input())
    t.append(tmp-1)
cnt = [-1 for j in range(26)]
now = 0
for i in range(D):
    cnt[t[i]] = i
    now += s[i][t[i]]
    tmp = 0
    for j in range(26):
        if j != t[i]:
            if cnt[t[i]] == -1:
                tmp += c[j] * (i + 1)
            else:
                tmp += c[j] * (i - cnt[j])
    now -= tmp
    print(now)