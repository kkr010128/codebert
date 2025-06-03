def main():
    N = int(input())
    A = list(map(int, input().split()))
    xor = 0
    for a in A:
        xor ^= a
    ans = [xor ^ a for a in A]
    print(*ans)


if __name__ == "__main__":
    main()
