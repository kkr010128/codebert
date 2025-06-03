N = input()
lenN = len(N)
sumN = 0

for x in N:
    sumN += int(x)
    if sumN > 9:
        sumN %= 9
if sumN % 9 == 0:
    print('Yes')
else:
    print('No')