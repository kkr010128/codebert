import sys
from operator import itemgetter
import math

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():

    a, b, x = mi()
    V = a**2 * b

    if V // 2 < x:
        X = 2*x / a**2 - b
        Y = b - X
        ans = math.degrees(math.asin(Y/math.sqrt(a**2 + Y**2)))
    else:
        X = 2*x / (a*b)
        ans = math.degrees(math.asin(b/math.sqrt(X**2 + b**2)))

    print(ans)

    return

main()
