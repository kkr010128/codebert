s = input()
n = len(s)
s2 = s[:(n-1)//2]
s3 = s[((n+3)//2)-1:]
if (s == s[::-1]) & (s2 == s2[::-1]) & (s3 == s3[::-1]):
    print("Yes")
else:
    print("No")