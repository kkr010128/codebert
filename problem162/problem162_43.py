n, m = map(int, input().split())

if n % 2 == 1:
    a = [i for i in range(1, m+1)]
    b = [i for i in reversed(range(m+1, 2*m+1))]
    ab = [(x, y) for x, y in zip(a, b)]
else:
    ab = []
    x, y = (n-1)//2, n//2
    if x % 2 != 0:
        x, y = y, x

    evenl = 1
    evenr = x
    while evenl < evenr:
        ab.append((evenl, evenr))
        evenl += 1
        evenr -= 1

    oddl = x+1
    oddr = n-1
    while oddl < oddr:
        ab.append((oddl, oddr))
        oddl += 1
        oddr -= 1

    ab = ab[:m]


for a, b in ab:
    print(a, b)