a, b = input().split()
s1 = a*int(b)
s2 = b*int(a)
print(s1 if s1 < s2 else s2)