import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    k = int(input())

    k2 = np.arange(1, k+1)
    k2gcd = np.gcd.outer(k2, np.gcd.outer(k2, k2))
    print(k2gcd.sum())

if __name__ == '__main__':
    main()