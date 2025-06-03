def main():
    N, A, B = list(map(int, input().split()))
    if (A ^ B) & 1:
        return min((A - 1) + 1 + (B - A - 1) // 2,
                   (N - B) + 1 + (N - (A + N - B + 1)) // 2)
    return (B - A) // 2

print(main())
