def main():
    N, X, Y = (int(i) for i in input().split())
    cnt = [0]*N
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            d = min(abs(i-j), abs(i-X)+1+abs(j-Y), abs(i-X)+abs(X-Y)+abs(j-Y))
            cnt[d] += 1
    for d in cnt[1:]:
        print(d)


if __name__ == '__main__':
    main()
