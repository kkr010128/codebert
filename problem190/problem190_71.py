s = input()
s1 = list(s[:((len(s)) - 1) // 2])
s2 = list(s[(len(s) + 2) // 2:])
if s1 == s2:
    print('Yes')
else:
    print('No')