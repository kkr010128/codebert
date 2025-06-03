import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def satisfaction(d, last, c):
    res = 0
    for i in range(26):
        res += c[i] * (d - last[i])
    return res


def main():
    d = I()
    c = LI()
    s = LIR(d)
    t = IR(d)
    last = [0] * 26
    satis = 0
    for day in range(d):
        j = t[day] - 1
        last[j] = day + 1
        satis += s[day][j]
        satis -= satisfaction(day + 1, last, c)
        print(satis)


main()
