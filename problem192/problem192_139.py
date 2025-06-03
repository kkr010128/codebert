def f(x):
    return x * (x - 1) // 2


n = int(input())
a = list(map(int, input().split()))
counter = [0] * n

for ai in a:
    ai -= 1
    counter[ai] += 1

m = 0
for c in counter:
    m += f(c)

for i, ai in enumerate(a):
    ai -= 1
    c = counter[ai]
    if c == 0:
        print(m)
    else:
        print(m - f(c) + f(c - 1))