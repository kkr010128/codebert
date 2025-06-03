s = list(input())

if s.count('R') == 3:
    print(3)
elif s.count('R') == 1:
    print(1)
elif s.count('R') == 0:
    print(0)
else:
    if s[1] == 'R':
        print(2)
    else:
        print(1)