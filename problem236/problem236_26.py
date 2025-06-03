import sys
import math
import bisect

def solve(s):
    n = len(s)
    if n % 2 == 1:
        return False
    for i in range(0, n, 2):
        if s[i:i+2] != 'hi':
            return False
    return True

def main():
    H = int(input())
    W = int(input())
    n = int(input())
    A = []
    for h in range(H + 1):
        for w in range(W + 1):
            val = H * w + h * W - h * w
            if val >= n:
                A.append(h + w)
    print(min(A))

if __name__ == "__main__":
    main()
