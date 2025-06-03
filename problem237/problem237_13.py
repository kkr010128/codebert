def main():
    N = int(input())
    L = []
    for i in range(N):
        xi, li = map(int, input().split())
        s = xi - li
        f = xi + li
        L.append((f, s))
    
    L.sort()

    ans = 0
    finish = -float("inf")
    for i in L:
        if finish <= i[1]:
            ans += 1
            finish = i[0] 

    print(ans)

if __name__ == "__main__":
    main()

