import sys
def solve():
    input = sys.stdin.readline
    N = int(input())
    if N == 2: print(1)
    else:
        K = {N, N-1}
        for i in range(2, N + 1):
            if i ** 2 > N: break
            if N % i == 0:
                k = N
                while k % i == 0:
                    k //= i
                if k % i == 1: K |= {i}
            
            if (N - 1) % i == 0:
                K |= {i}
                if i ** 2 != N - 1: K |= {(N - 1) // i}
        print(len(K))
        #print(K)
    return 0

if __name__ == "__main__":
    solve()