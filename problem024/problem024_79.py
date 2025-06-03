def is_leq_S(A, lim, K):
    S = [0] * K

    ai = 0
    si = 0

    while ai < len(A):
        if S[si] + A[ai] <= lim:
            S[si] += A[ai]
            ai += 1
        else:
            si += 1

            if si == K:
                return False
    
    return True


def main():
    N, K = [int(_) for _ in input().split()] 
    A = []
    
    for _ in range(N):
        A.append(int(input()))

    l = 0
    r = 100000 * 100000

    while l + 1 < r:
        m = (l + r) // 2

        if is_leq_S(A, m, K):
            S = m
            r = m
        else:
            l = m

    print(S)
    

main()
