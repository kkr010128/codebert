from statistics import median


def main():
    N = int(input())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    min_median = median(A)
    max_median = median(B)
    if N % 2 == 1:
        print(max_median - min_median + 1)
    else:
        print(round((max_median-min_median)*2)+1)


if __name__ == "__main__":
    main()
