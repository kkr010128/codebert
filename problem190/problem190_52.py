s = input()
n = len(s)


def check(r):
    if r == r[::-1]:
        return True


print("Yes" if check(s) and check(s[:(n-1)//2])
      and check(s[((n-1)//2) + 1:]) else "No")