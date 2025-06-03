def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    ans = []
    for i in range(k,n):
        ans.append("Yes" if a[i] > a[i-k] else "No")

    print("\n".join(ans))

if __name__ == '__main__':
    main()