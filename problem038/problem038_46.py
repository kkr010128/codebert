S = input()
L = S.split()
a = L[0]
a = int(a)
b = L[1]
b = int(b)
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
elif a == b:
    print('a == b')