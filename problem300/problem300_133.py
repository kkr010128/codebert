import fractions
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def prime_factorize(n):
    P = []
    P_set = set()
    while n % 2 == 0:
        P.append(2)
        P_set.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            P.append(f)
            P_set.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        P.append(n)
        P_set.add(n)

    P_count = {p:0 for p in P_set}
    for p in P: P_count[p] += 1

    return P_count


def solve(A: int, B: int):
    gcd = fractions.gcd(A,B)
    P = prime_factorize(gcd).keys()
    print(len(list(P))+1)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)



if __name__ == "__main__":
    main()
