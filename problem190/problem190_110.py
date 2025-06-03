s = input()
n = len(s)
sd = s[::-1]
a = s[:int((n-1)/2)]
ad = a[::-1]
b = s[int((n+3)/2-1):]
bd = b[::-1]
if s == sd and a == ad and b == bd:
    print('Yes')
else:
    print('No')
