n = int(input())
x = input()

popcount = x.count('1')
p = int(x, 2) % (popcount + 1)
q = int(x, 2) % (popcount - 1) if popcount != 1 else 0
for i in range(n):
    if x[i] == '0':
        y = (p + pow(2, n-i-1, popcount+1)) % (popcount + 1)
    else:
        if popcount != 1:
            y = (q - pow(2, n-i-1, popcount-1)) % (popcount - 1)
        else:
            print(0)
            continue
    cnt = 1
    while y != 0:
        y %= bin(y).count('1')
        cnt += 1
    print(cnt)
