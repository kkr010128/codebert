s = str(input())
t = str(input())
t_before = ''
for i in range(len(s)):
    t_before += t[i]

if s == t_before:
    print('Yes')
else:
    print('No')