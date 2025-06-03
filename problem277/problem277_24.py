import sys

import numpy as np

input = sys.stdin.readline


def main():
    H, W, K = map(int, input().split())
    s = np.zeros(shape=(H, W), dtype=np.bool)
    for i in range(H):
        s[i] = tuple(map(lambda x: True if x == "#" else False, input().rstrip()))

    ans = np.zeros(shape=(H, W), dtype=np.int64)
    h_keep = 0
    k = 1
    for h in range(H):
        if s[h].sum() > 0:
            indices = np.where(s[h])[0]
            ans[h_keep:h + 1] = k
            k += 1
            for idx in reversed(indices[:-1]):
                ans[h_keep:h + 1, :idx + 1] = k
                k += 1
            h_keep = h + 1
        else:
            h_keep = min(h_keep, h)

    if h_keep < H:
        h_base = h_keep - 1
        for h in range(h_keep, H):
            ans[h] = ans[h_base]

    for h in range(H):
        print(" ".join(map(str, ans[h])))


if __name__ == "__main__":
    main()
