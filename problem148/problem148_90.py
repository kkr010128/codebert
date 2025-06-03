def main():
    a, b, c, k = map(int, input().split())
    if a + b >= k:
        print(min(a, k))
    else:
        print(a-(k-a-b))

if __name__ == "__main__":
    main()