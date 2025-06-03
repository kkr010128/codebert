s = raw_input()
s = s.split(' ')

a, b = int(s[0]), int(s[1])

if 1 <= a <= 9 and 1 <= b <= 9:
    print a*b
else:
    print -1
