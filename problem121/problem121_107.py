import math


def solve():
    N = int(input())
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in range(len(str(N))):
        if N == 0:
            break
        j = N % 26
        N -= 1
        N = N // 26
        ans = lowercase[j - 1] + ans
    print(ans)


if __name__ == '__main__':
    solve()
