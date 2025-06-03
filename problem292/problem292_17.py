def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                ans += inlis[i] * inlis[j]
    print(ans)
    
    
    
if __name__ == "__main__":
    main()
