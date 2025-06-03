n = int(input())
s = input()

if n % 2 != 0:
    print("No")
else:
    h = n // 2
    print("Yes" if s[0:h] == s[h:] else "No")