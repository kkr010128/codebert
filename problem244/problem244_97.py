a = input()
k = int(a.split()[0])
x = int(a.split()[1])

if k * 500 >= x:
    print('Yes')
else:
    print('No')