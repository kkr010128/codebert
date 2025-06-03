N = input()

S = 0
for m in N:
    S += int(m)
    S %= 9

if S == 0:
    print('Yes')
else:
    print('No')