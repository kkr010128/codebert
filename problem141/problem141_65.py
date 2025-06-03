def main():
    n = int(input())
    a = list(map(int,input().split()))
    ki = [0 for i in range(n+1)]
    ki[0] = 1   
    for i in range(1,n+1):
        ki[i] = 2*(ki[i-1] - a[i-1])
        if ki[i]<=0:
            print(-1)
            return
    if ki[-1]<a[-1]:
        print(-1)
        return
    ki[-1] = a[-1]
    for i in range(n):
        ki[n-1-i] = min(ki[n-1-i],ki[n-i]+a[n-1-i])
    print(sum(ki))

if __name__ == "__main__":
    main()
