def get_cusum(lst):
    cusum = [0] + lst
    for i in range(1, len(cusum)):
        cusum[i] = cusum[i] + cusum[i-1]
    return cusum


def main():

    n, m, k = map(int, input().split(" "))
    book_a = get_cusum(list(map(int, input().split(" "))))
    book_b = get_cusum(list(map(int, input().split(" "))))
    ans = 0
    top = m

    # print(book_a)
    # print(book_b)

    for i in range(n + 1):
        if book_a[i] > k:
            break

        while book_b[top] > k - book_a[i]:
            top -= 1

        ans = max(ans, i+top)

    print(ans)


main()
