import sys
import math
import bisect


def main():
    n = int(input())
    ans = ((n+1)//2) / n
    print('%.10f' % ans)



if __name__ == "__main__":
    main()
