i = input()
a = input().split()
c = a[0]
d = a[0]
for j in range(int(i)):
    if int(c) > int(a[j]):
        c = int(a[j])

                
for j in range(int(i)):
    if int(d) < int(a[j]):
        d = int(a[j])

e = sum(int(o) for o in a)

print('{0} {1} {2}'.format(int(c),int(d),int(e)))
