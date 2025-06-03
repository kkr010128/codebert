n = input().split()
a = []
for i in range(len(n)):
  a.append(int(n[i]))
a = sorted(a)
print('{0} {1} {2}'.format(a[0],a[1],a[2]))