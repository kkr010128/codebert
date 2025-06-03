def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    x = 0
    for i in range(N):
        x ^= a[i]

    x ^= a[0]
    xors = [x]
    for i in range(1, N):
        x ^= a[i-1]
        x ^= a[i]
        xors.append(x)

    print(' '.join(str(x) for x in xors))


main()
