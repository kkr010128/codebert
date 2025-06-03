def check(r):
    if r == r[::-1]:
        return True


def main():
    s = input()
    n = len(s)
    print("Yes" if check(s) and check(s[:(n-1)//2])
          and check(s[((n-1)//2) + 1:]) else "No")


if __name__ == "__main__":
    main()