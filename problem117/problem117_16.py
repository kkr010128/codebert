from itertools import accumulate
from bisect import bisect_left,bisect_right

def main():
    n,m,k=map(int,input().split())
    a=[0]+list(accumulate(map(int,input().split())))
    b=[0]+list(accumulate(map(int,input().split())))

    result = 0
    for i in range(n+1):
        tmp = k - a[i]
        if tmp < 0:
            continue
        tmpNum = i + bisect_right(b, tmp) - 1
        if tmpNum > result:
            result = tmpNum

    print(result)       


if __name__ == "__main__":
    main()