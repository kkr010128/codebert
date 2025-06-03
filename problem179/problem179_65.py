# coding=utf-8

if __name__ == '__main__':
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    lisum = sum(li)

    cnt = 0
    for i in range(N):
        if lisum / (M * 4) <= li[i]:
            cnt += 1

    if M <= cnt:
        print('Yes')

    else:
        print('No')
