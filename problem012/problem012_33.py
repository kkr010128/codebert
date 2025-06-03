ans = 0
for i in xrange(input()):
    n = int(raw_input())
    if n <= 1:
        continue
    j = 2
    while j*j <= n:
        if n%j == 0:
            break
        j += 1
    else:
        ans += 1
print ans