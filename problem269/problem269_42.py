def solve(mid):
    pos = (d[0] + d[1]) * (mid // 2)
    if mid % 2 == 1:
        pos += d[0]

    if mid % 2 == 1:
        nxt_pos = pos + d[1]
    else:
        nxt_pos = pos + d[0]

    if pos * nxt_pos < 0 or nxt_pos == 0:
        return True
    else:
        return False

t = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

v0 = a[0] - b[0]
v1 = a[1] - b[1]
d = [t[0] * v0, t[1] * v1]

if d[0] == -d[1]:
    print("infinity")
    exit()
    
ok = 0
ng = 10 ** 60
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)

