import itertools
import functools
import operator
pi = functools.partial(functools.reduce, operator.mul)


def solve():
    N = int(input())
    d = [int(x) for x in input().split()]
    ans = 0
    for c in itertools.combinations(d, 2):
        # print(c)
        ans += pi(c)
    print(ans)


if __name__ == "__main__":
    solve()