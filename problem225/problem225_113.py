import sys
import math
from collections import deque
from collections import defaultdict

def main():
    n, k = list(map(int,sys.stdin.readline().split()))
    ans = n//k
    if n%k != 0:
        ans += 1
    print(ans)


    return 0
if __name__ == "__main__":
    main()