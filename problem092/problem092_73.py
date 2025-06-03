x, k, d = map(int, input().split())

if abs(x) >= k * d:
    print(abs(x) - k * d)
else:
    a = abs(abs(x) - (abs(x) // d) * d)
    k -= (abs(x) // d)
    if k % 2 == 0:
        print(a)
    else:
        print(abs(a - d))

