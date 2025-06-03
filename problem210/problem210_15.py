import bisect

n = int(input())
s = list(input())
q = int(input())

alphabet = [chr(ord('a') + i) for i in range(26)]

d = {alphabet[i]: [] for i in range(26)}
for i, a in enumerate(s):
    d[a].append(i)

ans = []
for i in range(q):
    query = input().split()

    if query[0] == '1':
        idx, c = int(query[1]) - 1, query[2]
        if s[idx] == c:
            continue
        d[s[idx]].remove(idx)
        bisect.insort_left(d[c], idx)
        s[idx] = c
    else:
        l, r = int(query[1]) - 1, int(query[2]) - 1
        res = 0
        for c in alphabet:
            if bisect.bisect_right(d[c], r) > bisect.bisect_left(d[c], l):
                res += 1
        ans.append(res)

for i in ans:
    print(i)