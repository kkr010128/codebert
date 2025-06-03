def allocation():
    n, k = map(int, input().split())
    w = []
    for i in range(n):
        w.append(int(input()))

    # 最大積載量pを算出
    min = 0
    max = 100000000000
    while min + 1 != max:
        mid =(min + max) // 2
        if check(n, k, w, mid):
            max = mid
        else:
            min = mid
    print(max)

def check(n, k, w, p):
    t = 0
    now = 0
    for i in range(n):
        if (w[i] > p):
            return False
        if (now + w[i] > p):
            t += 1
            now = w[i]
        else:
            now += w[i]
    if now > 0:
        t += 1
    if t > k:
        return False
    else:
        return True

if __name__ == '__main__':
    allocation()
