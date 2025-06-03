def main():
    n = int(input())
    if n%2==1:
        print(0)
        return
    md = 10
    cnt = 0
    while n>=md:
        cnt += n//md
        md = md*5
    print(cnt)

if __name__ == "__main__":
    main()
