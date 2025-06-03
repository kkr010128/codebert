import sys
input = sys.stdin.readline

h, w, kk = map(int, input().split())
ss = [[0 for _ in range(h)] for _ in range(w)]
for i in range(h):
    for j, c in enumerate(list(input().strip())):
        if c == '1':
            ss[j][i] = 1

ans = 100000
for i in range(2 ** (h - 1)):
    end = []
    for j in range(h - 1):
        if i & 2 ** j:
            end.append(j + 1)
    end.append(h)
    start = [0]
    for j in end:
        start.append(j)
    start.pop()
    sums = [0] * len(start)

    tans = len(start) - 1
    imp = False
    for j in range(w):
        reset = False
        for k, (s, e) in enumerate(zip(start, end)):
            sums[k] += sum(ss[j][s:e])
            if sums[k] > kk:
                reset = True
                break
        if reset:
            tans += 1
            for k, (s, e) in enumerate(zip(start, end)):
                sums[k] = sum(ss[j][s:e])
                if sums[k] > kk:
                    imp = True
        if imp:
            break
    if not imp:
        ans = min(ans, tans)

print(ans)
