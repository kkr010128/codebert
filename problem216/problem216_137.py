x = list(map(int , input().split()))
s = set()

for i in x:
    if i not in s:
        s.add(i)

if len(s) == 2:
    print('Yes')
else:
    print('No')