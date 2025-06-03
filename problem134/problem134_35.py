def main():
    N = int(input())
    A = list(map(int, input().split()))
    SUM = 1

    if 0 in A:
        print(0)
        return

    for a in A:
        SUM = SUM * a
        if SUM > 1000000000000000000:
            print(-1)
            return

    print(SUM)
main()