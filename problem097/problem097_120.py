k = int(input())
if k % 2 == 0 or k % 5 == 0:
    x = -1
else:
    m = 7
    n = 7
    x = 1
    while n % k != 0:
        m = (m * 10) % k
        n += m
        x += 1
print(x)