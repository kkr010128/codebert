def tri_num(num):
    num -= 1
    return int(num * (num + 1) / 2)


def main():
    n, m = map(int, input().split())
    print(tri_num(n) + tri_num(m))


if __name__ == "__main__":
    main()
