import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    A = LI()
    a = sorted(A,reverse=True)

    high = a[0] * 2 + 1
    low = 0
    while high > low + 1:
        mid = (high + low) // 2

        cnt = 0
        j = N - 1
        for i in range(N):
            while a[i] + a[j] < mid:
                j -= 1
                if j < 0: break
            else:
                cnt += (j+1)
                continue
            break
        if cnt <= M:
            high = mid
        else:
            low = mid

    s = [a[0]]
    for i in range(1,N):
        s.append(s[-1]+a[i])

    ans = 0
    cnt = 0
    m = a[0] * 2
    j = N - 1
    for i in range(N):
        while a[i] + a[j] < low:
            j -= 1
            if j < 0: break
        else:
            ans += a[i] * (j+1) + s[j]
            cnt += j + 1
            m = min(m,a[i] + a[j])
            continue
        break

    print(ans - (cnt-M) * low)


if __name__ == '__main__':
    main()