def solve(T, R, S, P, K):
    N = len(T)
    Z =[None for i in range(N)]
    for i in range(N):
        if T[i] == 'r':
            Z[i] = P
        elif T[i] == 's':
            Z[i] = R
        else:
            Z[i] = S
        if i - K >= 0:
            if T[i-K] == T[i] and Z[i-K] != 0:
                Z[i] = 0
    return sum(Z)
N, K = map(int,input().split(' '))
R, S, P = map(int,input().split(' '))
T = str(input())
print(solve(T, R, S, P, K))