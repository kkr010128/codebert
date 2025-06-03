def main():
    a,b,c = map(int,input().split())
    k = int(input())

    i = 0
    while a >= b:
        b *= 2
        i += 1
    while b >= c:
        c *= 2
        i += 1
    print("Yes" if i <= k else "No")

if __name__ == '__main__':
    main()