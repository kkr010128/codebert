def resolve():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    def isok(num):
        if num >= N:
            anum = N
            bnum = num-anum
        else:
            anum = num
            bnum = 0
        atotal = sum(A[:anum])
        btotal = sum(B[:bnum])
        if atotal + btotal <= K:
            return True
        i = 0
        while not (anum-1-i < 0 or bnum+i >= M):
            atotal -= A[anum-1-i]
            btotal += B[bnum+i]
            if atotal + btotal <= K:
                return True
            i += 1
        return False
    
    left = -1
    right = N+M+1
    while (right - left) > 1:
        mid = left + (right - left)//2
            
        if isok(mid):
            left = mid
        else:
            right = mid
    print(left)


if '__main__' == __name__:
    resolve()