# coding: utf-8

def check_divide(n):
    max_v = int(n ** (1/2))
    divide_nums = []
    for i in range(1,max_v + 1):
        if n % i == 0:
            divide_nums.append(i)
    return divide_nums

def check_divide2(n):
    divide_nums = []
    for K in range(2,n+1):
        tmp = n
        while True:
            if tmp % K ==0:
                tmp = tmp // K
            else:break
        if tmp % K == 1:
            divide_nums.append(K)
    return divide_nums

if __name__ == '__main__':
    N = int(input())
    tmp1 = check_divide(N-1)
    if tmp1[-1] ** 2 == N-1:
        tmp1 = len(tmp1) * 2 - 2
    else:
        tmp1 = len(tmp1) * 2 - 1

    candidates = check_divide(N)[1:]

    tmp2 = [N]
    for val in candidates:
        N_ = N
        while True:
            if N_ % val == 0:
                N_ = N_ / val
            else:break
        if N_ % val == 1:
            tmp2.append(val)
    tmp2 = len(tmp2)
    print(tmp1 + tmp2)