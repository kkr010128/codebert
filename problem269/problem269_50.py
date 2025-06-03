t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
a = a1 - b1
b = a2 - b2
if a < 0:
    a = -a
    b = -b
p = t1 * a + t2 * b
if p > 0:
    print(0)
    exit()
if p == 0:
    print('infinity')
    exit()
top = a * t1
p = -p
ans = (top // p + 1) * 2 - 1 - (top % p == 0)
print(ans)