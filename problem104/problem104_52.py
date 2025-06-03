def main():
    L, R, d = (int(i) for i in input().split())
    ans = R//d - (L-1)//d
    print(ans)


if __name__ == '__main__':
    main()
