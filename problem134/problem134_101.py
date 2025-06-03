# coding=utf-8
import sys

if __name__ == '__main__':
    N = int(input())
    li_A = list(map(int, input().split()))

    ans = li_A[0]

    if 0 in li_A:
        print('0')
        sys.exit()

    for i in range(1, N):
        if ans * li_A[i] > 1000000000000000000:
            print('-1')
            sys.exit()
        else:
            ans *= li_A[i]

    print(ans)

