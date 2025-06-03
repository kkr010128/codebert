def solve():
    a, b = input().split()
    if a > b:
        print(b*int(a))
    else:
        print(a*int(b))


if __name__ == '__main__':
    solve()
