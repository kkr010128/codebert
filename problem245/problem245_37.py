#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(N: int, S: str):
    T = S.replace("ABC","")
    ans = N - len(T)
    ans //= 3

    print(ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)



if __name__ == "__main__":
    main()
