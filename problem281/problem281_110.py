# from math import factorial

def main():
    x, y = map(int, input().split())
    # m = (i+2, j+1)
    # n = (i+1, j+2)
    # x = 2m + n
    # y = m + 2n
    # 2x - y = 3m
    # 2y - x = 3n

    m = (2*x-y) // 3
    n = (2*y-x) // 3
    def cmb(n, r, mod):
        if (r<0 or r>n):
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] * finv[n-r] % mod

    mod = 10**9+7 #素数制限
    N = m+n
    fac = [1, 1] # 元テーブル
    finv = [1, 1] # 逆元テーブル
    finv_cal = [0, 1] #逆元計算用

    for i in range(2, N + 1):
        fac.append((fac[-1] * i) % mod)
        finv_cal.append((-finv_cal[mod % i] * (mod//i)) % mod)
        finv.append((finv[-1] * finv_cal[-1]) % mod)
    
    # 行き先のx+yが3の倍数でないとたどり着けない。
    if (x+y) % 3 != 0:
        print(0)
    else:
        # m, n どちらかが負かもしくはどちらも0の時
        if m < 0 or n < 0 or (m+n) == 0:
            print(0)
        else:
            ans = cmb(m+n, n, mod)           
            print(ans)


if __name__ == '__main__':
    main()