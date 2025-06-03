def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    if 0 in A:
        print(0)
        return

    mul = 1
    for a in A:
        mul *= a

        if mul > 1e18:
            print(-1)
            return

    print(mul)


main()