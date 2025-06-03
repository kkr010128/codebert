n = [int(x) for x in input()]
s = sum(n)
if s % 9 == 0:
    print('Yes')
else:
    print('No')