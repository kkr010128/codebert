def main():
    n = int(input())
    c = input()
    r = 0
    for i in range(n):
        if c[i]=='R':
            r += 1
    ans = 0
    for i in range(r):
        if c[i]=='W':
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
