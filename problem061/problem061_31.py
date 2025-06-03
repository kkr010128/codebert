string = input()

for s in string:
    if s.isupper():
        print(s.lower(), end='')
    else:
        print(s.upper(), end='')
print('')