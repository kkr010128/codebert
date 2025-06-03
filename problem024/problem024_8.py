def ok(p, ws, n, k):
    track = 1
    now = 0
    for i in range(n):
        if ws[i] > p:
            return False
        if now + ws[i] > p:
            track += 1
            now = ws[i]
        else:
            now += ws[i]
    if track > k:
        return False
    else:
        return True


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ws = []
for _ in range(n):
    ws.append(int(input()))

p_min = 0
p_max = int(1e+10)
while p_min < p_max:
    p = (p_min + p_max) // 2
    if ok(p, ws, n, k):
        p_max = p
    else:
        p_min = p + 1
print(p_max)
