from sys import stdin

s = stdin.readline().rstrip()

print("Yes" if s[2] == s[3] and s[4] == s[5] else "No")