def main():
    n,m = map(int, input().split())
    a = sorted(list(map(int, input().split())),reverse = True)
    all = sum(a)
    cnt = 0
    for i in(a):
        if(i * 4 * m >= all and cnt < m):
            cnt += 1
    if cnt >= m:
        print('Yes')
    else:
        print('No')
main()