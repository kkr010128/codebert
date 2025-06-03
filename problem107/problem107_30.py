def main():
    N = int(input())
    X = input()
    XINT = int(X,2)
    ANS = [0]*N
    TEMP = [0]*N
    CHAIND = [0]*N

    cnt = count_ones_by_bitmask(XINT)
    
    if cnt == 0:
        for i in range(N):
            print(1)
            return
    if cnt ==1:
        for i in  range(N):
            if X[i] == '1':
                print(0) #全てが0になる
            else:
                if i==N-1:
                    print((int(X[N-1])+1)%2+1) # 2の剰余の反転
                else:
                    print((int(X[N-1]))%2+1) # 2の剰余
        return

    p = XINT % (cnt+1)
    m = XINT % (cnt-1)
    pmod = 1
    mmod = 1
    for i in range(N):
        ANS[i] = 1
        if (X[N-i-1] == '0'):
            TEMP[i] = (p + pmod) % (cnt+1)
        else:
            TEMP[i] = (m - mmod) % (cnt-1)
        pmod = (pmod*2) % (cnt+1)
        mmod = (mmod*2) % (cnt-1)


    CHA = list(set(TEMP))

    for i in range(len(CHA)):
        an = 0
        cha = CHA[i]
        cnt = count_ones_by_bitmask(CHA[i])
        while cnt>0:
            an += 1
            cha = cha%cnt
            cnt = count_ones_by_bitmask(cha)
        CHAIND[CHA[i]] = an

    for i in reversed(range(N)):
        print(ANS[i]+CHAIND[TEMP[i]])


def count_ones_by_bitmask(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

if __name__ == '__main__':
    main()
