x, k, d = map(int, input().split())
x = abs(x)
if x > k*d:
    print(x-k*d)
else:
    p = x//d
    c = k-p
    if (c%2 == 0):
        print(abs(x-p*d))
    else:
        print(abs(d-abs(x-p*d)))
