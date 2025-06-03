from math import ceil
def main():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    C.sort()
    def chk(x):
        cnt = 0
        for i in range(N):
            cnt += max(ceil(A[i]-x/C[i]), 0)
            if cnt > K:
                return False
        return True
    ng, ok = -1, 10**12
    while ok - ng > 1:
        m = (ok+ng)//2
        if chk(m):
            ok = m
        else:
            ng = m
    print(ok)
if __name__ == "__main__":
    main()