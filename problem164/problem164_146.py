def main():
    abcd = [int(_x) for _x in input().split()]
    a = abcd[0]
    b = abcd[1]
    c = abcd[2]
    d = abcd[3]

    while True:
        c = c - b
        if c <= 0:
            print("Yes")
            return
        a = a - d
        if a <= 0:
            print("No")
            return


main()
