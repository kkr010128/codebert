def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())

    d = abs(A - B)
    s = V - W
    print('YES' if T * s >= d else 'NO')


if __name__ == '__main__':
    main()
