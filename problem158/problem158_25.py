def Qa():
    k = int(input())
    a, b = map(int, input().split())

    lis = range(a, b + 1)
    ans = 'NG'
    for v in lis:
        if v % k == 0:
            ans = 'OK'
    print(ans)

if __name__ == '__main__':
    Qa()
