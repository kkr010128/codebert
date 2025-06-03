#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, S: "List[str]"):
    s_plus = []
    s_minus = []
    total = 0
    last = 0
    for s in S:
        l = 0
        r = 0
        for v in s:
            if v == '(':
                l += 1
            elif v == ')':
                if l > 0:
                    l = l - 1
                else:
                    r += 1
        # if r == 0:
        #     total += l
        # elif l ==0:
        #     last += r
        if l >= r:
            s_plus.append([l, r])
        else:
            s_minus.append([l, r])

    s_plus.sort(key=lambda x: x[1])
    s_minus.sort(key=lambda x: -x[0])
    # print(s_plus, s_minus)
    total = 0
    for l, r in s_plus + s_minus:
        total -= r
        if total < 0:
            print(NO)
            return
        total += l
    if total == 0:
        print(YES)
    else:
        print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
