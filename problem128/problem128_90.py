import bisect as bi

if __name__ == '__main__':

    x,n = map(int,input().split())
    A = list(map(int,input().split()))
    B = [i for i in range(102)]
    
    #差分を求める
    C = list(set(B) - set(A))

    #二分探索自身の位置を調べる
    ind = bi.bisect_left(C,x)

    if ind == 0:
        print(C[0])
    elif ind == x - n:
        print(C[ind])
    else:
        tmp_l = abs(C[ind-1] - x)
        tmp_r = abs(C[ind] - x)
        if tmp_l > tmp_r:
            print(C[ind])
        else:
            print(C[ind-1])
