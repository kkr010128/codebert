s = input()
l = len(s)
a = s[0:(l-1)//2]
b = len(a)
print("Yes" if s == s[::-1] and a == a[::-1] else "No")