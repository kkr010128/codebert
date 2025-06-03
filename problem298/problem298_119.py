def main():
    n, k = map(int,input().split())
    inlis = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if inlis[i] >= k:
            ans += 1

    print(ans)
    
    
    
if __name__ == "__main__":
    main()
