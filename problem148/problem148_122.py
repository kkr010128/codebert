def maximum():
    A,B,C,K = map(int,input().split())
    num = 0
    max = 0
    if A <= K:
        max = A
        num = K - A
        if B <= num:
            num = num - B
            max -= num
            print(max)
            return
        else:
            print(max)
            return
    else:
        print(K)
        return
maximum()
