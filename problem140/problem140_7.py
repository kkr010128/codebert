import sys


RS = lambda: sys.stdin.readline()[:-1]
RI = lambda x=int: x(RS())
RA = lambda x=int: map(x, RS().split())
RSS = lambda: RS().split()


def solve():
    ans = []
    for i in s:
        if i == "P":
            ans.append("P")
        else:
            ans.append("D")
    print("".join(ans))
    return



s = RS()
solve()