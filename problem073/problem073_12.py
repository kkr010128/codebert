
def main():
    N = int(input())
    num = 0
    B = 1

    for A in range(1, N):
        for B in range(1, N):
            if N - A * B >= 1:
                num = num + 1
            else:
                break

    print(num)


main()
