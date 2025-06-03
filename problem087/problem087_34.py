n = input()
s = 0
for i in range(len(n)):
    s += int(n[i])
if s % 3 == 0:
    print('Yes')
else:
    print('No')
