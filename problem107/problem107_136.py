def main():
    N = int(input())
    X = input()
    
    def popcount(x):
        '''xの立っているビット数をカウントする関数
        (xは64bit整数)'''

        # 2bitごとの組に分け、立っているビット数を2bitで表現する
        x = x - ((x >> 1) & 0x5555555555555555)

        # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
        x = x + (x >> 8) # 16bitごと
        x = x + (x >> 16) # 32bitごと
        x = x + (x >> 32) # 64bitごと = 全部の合計
        return x & 0x0000007f

    ans = []
   
    f = [0] * N
    # preprocess 1
    for i in range(1, N):
        pc = popcount(i)
        j =  i % pc
        f[i] = f[j] + 1
    
    # preprocess 2
    X_COUNT = X.count("1")
    X = tuple(map(int, tuple(X)))
    rem_plus = [0] * N
    rem_minus = [0] * N
    two_factor = 1
    for i in range(N):
        rem_plus[i] = two_factor
        two_factor *= 2
        two_factor %= (X_COUNT+1)

    if X_COUNT > 1:
        two_factor = 1
        for i in range(N):
            rem_minus[i] = two_factor
            two_factor *= 2
            two_factor %= (X_COUNT-1)


    X_rem_plus = 0
    X_rem_minus = 0
    two_factor = 1
    for c in X[::-1]:
        X_rem_plus += two_factor*c
        X_rem_plus %= (X_COUNT+1)
        two_factor *= 2
        two_factor %= (X_COUNT+1)
    
    if X_COUNT > 1:
        two_factor = 1
        for c in X[::-1]:
            X_rem_minus += two_factor*c
            X_rem_minus %= (X_COUNT-1)
            two_factor *= 2
            two_factor %= (X_COUNT-1)
    
    for i, c in enumerate(X):
        if c:
            if X_COUNT > 1:
                rem = X_rem_minus - rem_minus[N-1-i]
                rem %= (X_COUNT-1)
                ans.append(f[rem]+1)
            elif X_COUNT == 1:
                ans.append(0)
            else:
                ans.append(0)
        else:
            rem = X_rem_plus + rem_plus[N-1-i]
            rem %= (X_COUNT+1)
            ans.append(f[rem]+1)
   
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()