def resolve():
    X = int(input())
    m = 100
    cnt = 0
    while m < X:
        m += m//100
        cnt += 1
    print(cnt)


if '__main__' == __name__:
    resolve()