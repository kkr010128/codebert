import sys
input = sys.stdin.readline
from math import sqrt
def main():
    N = int(input())
    A = [0]*(N+1)
    n = int(sqrt(N)) + 1
    for x in range(1, n):
        for y in range(1, n):
            for z in range(1, n):
                tmp = x*x + y*y + z*z + x*y + y*z + z*x
                if tmp <= N:
                    A[tmp] += 1
    for i in range(1,N+1):
        print(A[i])

if __name__ == '__main__':
    main()