a,b = (int(x) for x in input().split())
i = a - b * 2
if i <= 0:
    print('0')
else:
    print(i)
