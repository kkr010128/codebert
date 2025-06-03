def main():
    n = int(input())
    a = sorted(list(map(int,input().split())),reverse=True)
    ans = a[0]
    for i in range(3,n+1):
        if i%2==0:
            ans += a[i//2-1]
        else:
            ans += a[(i-1)//2]
    print(ans)

if __name__ == "__main__":
    main()
