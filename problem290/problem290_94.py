def main():
    import numpy as np
    import sys
    input = sys.stdin.readline
    N, K = map(int,input().split())
    A = np.sort(list(map(int,input().split())))
    F = np.sort(list(map(int,input().split())))[::-1]

    if K >= np.sum(A)*N:
        print(0)
        exit()
    ma = A[-1]*F[0]
    mi = 0
    A = A*F
    while ma != mi:
        tgt = (ma + mi)//2
        tmp = np.ceil((A-tgt)/F)
        if np.sum(tmp[tmp>0]) <= K:
            ma = (ma + mi)//2
        else:
            mi = (ma + mi)//2+1
    print(ma)
if __name__ == '__main__':
    main()
