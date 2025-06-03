import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
def resolve():
    N, M = lr()
    if N%2 == 1:
        for i in range(0, M):
            print(f'{2+i} {1+2*M-i}')
    else:
        k = N//4
        for i in range(M):
            if i < k:
                print(f'{i+1} {N-i}')
            else:
                print(f'{i+2} {N-i}')
resolve()