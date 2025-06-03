s = list(input())

f1 = s == list(reversed(s))
f2 = s[:(len(s)-1)//2] == list(reversed(s[:(len(s)-1)//2]))
f3 = s[(len(s)+2)//2:] == list(reversed(s[(len(s)+2)//2:]))
print("Yes" if all([f1, f2, f3]) else "No")