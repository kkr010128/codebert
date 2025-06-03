n = int(input())
s = input()


def some(s):
    a, b = s[:n//2], s[n//2:]
    if n % 2 or a != b: return "No"

    return "Yes"


print(some(s))