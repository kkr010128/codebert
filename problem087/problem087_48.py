s = str(input())
sm = 0
for c in s:
    sm += int(c)

if sm % 9 == 0:
    print('Yes')
else:
    print('No')