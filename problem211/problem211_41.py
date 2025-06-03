def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r-100*(n-10))

if __name__ == "__main__":
    main()
