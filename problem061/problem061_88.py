S = list(input())
for c in S:
    if c.isalpha():
        if c.isupper():
            print(c.lower(), end='')
        else:
            print(c.upper(), end='')
    else:
        print(c, end='')
print()

