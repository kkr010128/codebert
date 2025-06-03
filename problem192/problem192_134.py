# D - Banned K
from collections import Counter


def main():
    N, *A = map(int, open(0).read().split())
    cnt = Counter(A)
    total = sum(v * (v - 1) // 2 for v in cnt.values())
    res = [total - (cnt[a] - 1) for a in A]
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
