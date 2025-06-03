import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    X, Y, A, B, C = map(int, input().split())
    p = sorted(list(map(int, input().split())), reverse=True)
    q = sorted(list(map(int, input().split())), reverse=True)
    r = sorted(list(map(int, input().split())))

    ans = []
    ans += p[:X]
    ans += q[:Y]
    ans.sort(reverse=True)

    #print(ans, r)

    cl = 0
    while len(ans) and len(r):
        if ans[-1] < r[-1]:
            cl += r[-1]
            ans.pop(-1)
            r.pop(-1)
        else:
            break

    #print(ans, cl)
    print(sum(ans) + cl)


if __name__ == '__main__':
    solve()
