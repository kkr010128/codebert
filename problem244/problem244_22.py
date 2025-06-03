#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


YES = "Yes"  # type: str
NO = "No"  # type: str

INF=10**20
def solve(K: int, X: int):
    print(YES if K*500 >= X else NO)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)



if __name__ == "__main__":
    main()
