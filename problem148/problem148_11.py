from sys import exit

a, b, c, k = map(int, input().split())
total = 0
if a >= k:
    print(k)
    exit()
else:
    total += a
    k -= a
    if b >= k:
        print(total)
        exit()
    else:
        k -= b
        print(total - k)