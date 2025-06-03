n, *s = open(0).read().split()
n = int(n)

c0 = s.count('AC')
c1 = s.count('WA')
c2 = s.count('TLE')
c3 = n - (c0 + c1 + c2)

print('AC x ' + str(c0), 'WA x ' + str(c1), sep='\n')
print('TLE x ' + str(c2), 'RE x ' + str(c3), sep='\n')
