n = input()
x = input()
if n == x[:-1]:
    if len(x) - len(n) == 1:
        print('Yes')
else:
    print('No')