s = input()
if s == 'RRR':
    print(3)
elif s[:2] == 'RR' or s[1:] == 'RR':
    print(2)
elif s.count('R') >= 1:
    print(1)
else:
    print(0)