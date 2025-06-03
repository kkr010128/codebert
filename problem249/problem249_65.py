def main():
    A, B, K = map(int, input().split())

    if A - K > 0:
        print(A - K, B)
    elif B + A - K > 0:
        print(0, B + A - K)
    else:
        print(0, 0)


main()
