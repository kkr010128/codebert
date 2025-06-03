N = int(input())

v = 0

for c in str(N):
    v += int(c)

if v % 9 == 0:
    print('Yes')
else:
    print('No')