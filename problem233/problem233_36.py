def main():
    N = int(input())
    m = float("inf")
    ans = 0

    for i in [int(j) for j in input().split()]:
        if i < m:
            m = i
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()