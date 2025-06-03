N = int(input())
ans = 0
if N % 2 == 1:
    pass
else:
    two = 0
    five = 0
    tmp = 2
    while tmp <= N:
        two += N // tmp
        tmp *= 2
    tmp = 10
    while tmp <= N:
        five += N // tmp
        tmp *= 5
    ans = min(two, five)
print(ans)