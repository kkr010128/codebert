def main():
    H1, M1, H2, M2, K = map(int, input().split())
    ans = max((H2 * 60 + M2) - (H1 * 60 + M1) - K, 0)
    print(ans)


if __name__ == "__main__":
    main()
