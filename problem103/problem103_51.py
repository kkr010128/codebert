def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 1000
    for i in range(n-1):
        if a[i] < a[i+1]:
            res = res % a[i] + (res//a[i])*a[i+1]
    print(res)


if __name__ == '__main__':
    solve()
