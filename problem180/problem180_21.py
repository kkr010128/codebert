n, k = map(int, input().split())

t = n // k
re = n - t * k

i = True

while i == True:
    if abs(re - k) < re:
        re = abs(re - k)
        i = True
    else:
        i = False

print(re)
