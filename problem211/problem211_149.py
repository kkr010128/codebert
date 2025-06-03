import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    if n < 10:
        m += 100 * (10 - n)
    print(m)

if __name__ == "__main__":
    main()
