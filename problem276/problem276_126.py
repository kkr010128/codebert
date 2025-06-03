import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(input())
    A = np.array(input().split(), np.int64)
    B = np.append(0, A.cumsum())
    C = A[::-1].cumsum()
    C = np.append(C[::-1], 0)
    print(np.abs(B-C).min())



if __name__ == '__main__':
    main()