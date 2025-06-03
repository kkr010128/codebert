import sys

input = sys.stdin.readline


def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    D1 = T1 * A1 + T2 * A2
    D2 = T1 * B1 + T2 * B2

    if D1 == D2:
        print('infinity')
    else:
        if D2 > D1:
            A1, B1 = B1, A1
            A2, B2 = B2, A2
            D1, D2 = D2, D1
        M1 = T1 * A1
        M2 = T1 * B1
        if M1 > M2:
            print(0)
        else:
            cnt = (M2 - M1) // (D1 - D2)
            ans = cnt * 2
            diff = (M2 - M1) % (D1 - D2)
            if diff > 0:
                ans += 1
            print(ans)


if __name__ == '__main__':
    main()
