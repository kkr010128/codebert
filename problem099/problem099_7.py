def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    L, R = 0, max(arr)
    while L+1 < R:
        P = (L+R+1)//2
        cnt = 0
        for a in arr:
            if P < a:
                if a % P == 0:
                    cnt += a//P - 1
                else:
                    cnt += a//P
        if cnt <= k:
            R = P
        else:
            L = P
    print(R)

if __name__ == "__main__":
    main()
