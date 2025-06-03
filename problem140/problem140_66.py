pd = list(input())
for i in range(len(pd)):
    if '?' in pd[i]:
        pd[i] = 'D'
    print(pd[i], end = '')