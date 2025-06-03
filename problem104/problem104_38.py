def main():
    L, R, d = map(int, input().split())
    ans = R//d - (L-1)//d
    print(ans)


if __name__ == "__main__":
    main()
