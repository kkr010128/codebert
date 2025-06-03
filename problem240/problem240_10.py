n, m = list(map(int, input().split()))
ac = [0] * n
wa = [0] * n
penalty = 0
for i in range(m):
    p, s = list(input().split())
    p = int(p)
    if s == "AC" and ac[p - 1] == 0:
        ac[p - 1] = 1
        penalty += wa[p - 1]
    if s == "WA":
        wa[p - 1] += 1
print(sum(ac), penalty)