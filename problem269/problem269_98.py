t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
first = a1 * t1 - b1 * t1
second = (a2 * t2 - b2 * t2)
last = second + first
if first * last > 0:
    ans = 0
elif (abs(last) == 0):
    ans = 'infinity'
else:
    s = abs(first) // abs(last)
    t = abs(first) % abs(last)
    ans = 2 * s
    if t != 0:
        ans += 1
print(ans)