from math import gcd

def setwise_coprime_check_fun(A_list, N):
    gcd_all = A_list[0]
    for i in range(N - 1):
        gcd_all = gcd(gcd_all, A_list[i + 1])
        if gcd_all == 1:
            break
    return gcd_all

def preprocess_fun(A_max):
    p_flg = [True] * (A_max + 1)
    D = [0] * (A_max + 1)
    p_flg[0] = False
    p_flg[1] = False
    for i in range(2, A_max + 1, 1):
        if p_flg[i]:
            for j in range(i, A_max + 1, i):
                p_flg[j] = False
                D[j] = i
    return D

def pairwise_coprime_check(A_list, D, A_max):
    p_count = [0] * (A_max + 1)
    for A in A_list:
        temp = A
        d = 0
        while temp != 1:
            if p_count[D[temp]] == 1 and d != D[temp]:
                return 0
            p_count[D[temp]] = 1
            d = D[temp]
            temp = temp // D[temp]
    return 1

## 標準入力
N = int(input())
A_list = list(map(int, input().split(" ")))

# 整数の最大値を取得
A_max = max(A_list)

# 本体
if(setwise_coprime_check_fun(A_list, N) != 1):
    print("not coprime")
else:
    D = preprocess_fun(A_max)
    if pairwise_coprime_check(A_list, D, A_max) == 1:
        print("pairwise coprime")
    else:
        print("setwise coprime")