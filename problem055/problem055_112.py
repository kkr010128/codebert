n = int(input())
h = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for _ in range(n):
    b, f, r, v = [int(e) for e in input().split()]
    h[b-1][f-1][r-1] += v
for i, b in enumerate(h):
    if i != 0:
        print('#'*20)
    for f in b:
        print(' ', end='')
        print(*f)