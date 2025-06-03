def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    MOD = 10**9+7


    B = []
    flg_m = 0
    flg_p = 0

    for a in A:
        if a < 0:
            B.append([abs(a),-1])
            flg_m = 1
        else:
            B.append([abs(a),1])
            flg_p = 1

        b = 0
    ans = -10**9
    if k == 1:
        for a in A:
            ans = max(ans,a)
        print(ans)
        exit()

    B.sort(reverse=True)
    # print(B)
    if flg_p == 0 and k%2 == 1:
        B.sort()
        L = B[:k]
        ans = cal_ans(L)
        ans *=-1
        print(ans%MOD)
        exit()
    elif flg_p * flg_m == 0:
        L = B[:k]
        ans = cal_ans(L)
        print(ans)
        exit()

    flg_p = 0
    flg_m = 0
    flg_lm = 0
    flg_lp = 0
    # print(B)
    for i,(n,sign) in enumerate(B):
        if i < k:
            if sign == -1:
                flg_lp = 1
                last_m = n
            else:
                flg_lm = 1
                last_p = n
        else:
            if sign == -1:
                if flg_m == 0:
                    first_m = n
                    flg_m = 1
            else:
                if flg_p == 0:
                    first_p = n
                    flg_p = 1

    L = B[:k]
    ans = cal_ans(L)
    c = 0
    for n,sign in L:
        if sign == -1:
            c += 1
    if c % 2 == 0:
        print(ans)
        exit()
    if flg_p == 1 and flg_m == 1 and flg_lp == 1 and flg_lm == 1:
        if first_p * last_p >= first_m*last_m:
            a = first_p
            b = last_m
        else:
            a = first_m
            b = last_p
    elif flg_p == 1:
            a = first_p
            b = last_m
    elif flg_m == 1:
            a = first_m
            b = last_p
    else:
        ans = 1
        for a in A:
            ans *= a
            ans %= MOD
        print(ans)
        exit()


    ans *= a
    ans %= MOD
    ans *= pow(b,MOD-2,MOD)
    ans %= MOD
    print(ans)

def cal_ans(L):
    MOD = 10**9+7
    ans = 1
    for i,j in L:
        ans *= i
        ans %= MOD
    return ans



main()