def main():
    N, A, B = map(int, input().split())
    if A % 2 == B % 2:
        return abs(A - B)//2
    else:
        x = A + (B - A - 1)//2
        y = (N - B) + (- A + B + 1)//2
        return min(x, y)

print(main())
