#!/usr/bin/env python3
def main():
    import sys
    import numpy as np

    input = sys.stdin.readline

    A, B, H, M = map(int, input().split())

    pi = np.pi
    time = 60 * H + M
    theta_H = (time * 2 * pi) / (12 * 60)
    theta_M = (M * 2 * pi) / 60
    res = abs(theta_H - theta_M)
    theta = min(res, 2 * pi - res)
    ans = np.sqrt(A ** 2 + B ** 2 - 2 * A * B * np.cos(theta))
    print(ans)


if __name__ == '__main__':
    main()
