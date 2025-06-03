def is_palindrome(s):
    return s == s[::-1]


def main():
    s = "-" + input()
    n = len(s) - 1
    if (
        is_palindrome(s[1:])
        and is_palindrome(s[1 : (n - 1) // 2 + 1])
        and is_palindrome(s[(n + 3) // 2 : n + 1])
    ):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
