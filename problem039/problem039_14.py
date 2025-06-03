data = input()
a, b, c = [int(i) for i in data.split()]

if a < b < c:
    print('Yes')
else:
    print('No')