n, *a = map(int, open(0).read().split())
a.sort()
if a[0] == 0:
    print(0)
    exit()
b = 1
for c in a:
    b *= c
    if b > 10 ** 18:
        print(-1)
        exit()

print(b)
