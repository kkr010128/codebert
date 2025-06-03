def solve(x):
    cnt = 1
    while x > 0:
        x %= bin(x).count('1')
        cnt += 1
    return cnt

n = int(input())
x = input()
one = sum(map(int, list(x)))
num = int(x, 2)

up = num%(one+1)
if one == 1:
    down = 0
else:
    down = num%(one-1)

for i in range(n):
    if x[i] == '1':
        if one == 1:
            print(0)
            continue
        s = (down - pow(2, n-i-1, one-1))%(one-1)
    else:
        s = (up + pow(2, n-i-1, one+1))%(one+1)
    print(solve(s))