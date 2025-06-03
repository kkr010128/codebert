import sys
#import math


# input = sys.stdin.readline

def binary_search(arr, key,j):
    ok = j
    ng = len(arr)

    while abs(ok - ng) > 1:
        mid = int((ok + ng) / 2)

        if arr[mid] < key:
            ok = mid
        else:
            ng = mid

    return ok


def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans =0
    for i in range(N-2):
        for j in range(i+1,N-1):
            ok = binary_search(L,L[i]+L[j],j)
            ans += ok-j
    print(ans)
if __name__ == "__main__":
    main()
