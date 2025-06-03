s = input()
n = len(s)
entire = s == s[::-1]
left = s[:int((n-1)/2)] == s[:int((n-1)/2)][::-1]
right = s[int((n+3)/2-1):] == s[int((n+3)/2-1):][::-1]
if entire and left and right:
    print("Yes")
else:
    print("No")