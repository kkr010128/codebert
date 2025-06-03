# C - Marks
def main():
    N, K, *A = map(int, open(0).read().split())
    res = ["Yes" if tail > top else "No" for top, tail in zip(A, A[K:])]
    print("\n".join(res))


if __name__ == "__main__":
    main()
