x, n = map(int, input().split())
p = list(map(int, input().split()))
ans = 9999999999
lists = []
if n == 0:
    print(x)
    exit()
for i in range(-1000, 1000):
    if not i in p:
        lists.append(i)
for i in lists:
    if ans > abs(x - i):
        ans = abs(x-i)
        m = i
print(m)