import math
import fractions
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def get_lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


def solve(N: int, M: int, A: "List[int]"):
    lcm = A[0]
    for i,a in enumerate(A[1:]):
        lcm = get_lcm(a,lcm)

    if lcm % 2 == 1:
        print(0)
        exit()

    for i,a in enumerate(A):
        b = lcm // a
        if b % 2 == 0:
            print(0)
            exit()
        
    ans = math.floor(M/lcm+1/2) - math.ceil(1/lcm+1/2) + 1
    print(ans)

    
    
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)



if __name__ == "__main__":
    main()
