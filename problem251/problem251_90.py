import sys
import itertools


def resolve(in_):
    N, K = map(int, next(in_).split())
    R, S, P = map(int, next(in_).split())
    T = next(in_).rstrip()
    r = ord(b'r')
    s = ord(b's')
    p = ord(b'p')

    temp = [0] * (N + 1)

    ans = 0
    for i, v in enumerate(T):
        j = i - K
        if j < 0:
            if v == r:
                ans += P
                temp[i] = p
            elif v == s:
                ans += R
                temp[i] = r
            elif v == p:
                ans += S
                temp[i] = s
        else:
            if v == r and temp[j] != p:
                ans += P
                temp[i] = p
            elif v == s and temp[j] != r:
                ans += R
                temp[i] = r
            elif v == p and temp[j] != s:
                ans += S
                temp[i] = s
    
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
