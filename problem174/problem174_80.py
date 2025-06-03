import math
import sys

def main():
    n = int(sys.stdin.readline())

    total = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                total += math.gcd(i, math.gcd(j,k))

    print(total)

main()