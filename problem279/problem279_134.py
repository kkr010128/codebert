lst = [input() for i in range(2)]

n = int(lst[0])
s = lst[1]
t = ''

for i in range(n//2):
    t += s[i]

if n % 2 == 1:
    print('No')
elif t + t == s:
    print('Yes')
else:
    print('No')
