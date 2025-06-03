N = int(input())

if (N%2 == 1):
    print(0)
elif N == 0:
    print(0)
else:
    N //= 2
    res = 0
    div_coef = 1
    while True:
        tmp_add = N // (5 ** div_coef)
        res += int(tmp_add)
        div_coef += 1
        # print(int(tmp_add))
        if tmp_add < 1:
            break
    # print(N)
    print(int(res))
