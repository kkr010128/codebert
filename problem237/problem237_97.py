def main():
    n = int(input())
    A = []
    for _ in range(n):
        x, l = map(int, input().split())
        A.append([x - l, x + l])
    A.sort(key = lambda x: x[1])
    ans, lmax = 0, -10 ** 11
    for a in A:
        if lmax <= a[0]:
            ans += 1
            lmax = a[1]
    print(ans)

if __name__ == '__main__':
    main()
