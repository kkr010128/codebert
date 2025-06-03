
n = int(input())
s = [str(input()) for i in range(n)]

a = s.count(('AC'))
b = s.count(('WA'))
c = s.count(('TLE'))
d = s.count(('RE'))

print("AC x {}".format(a))
print("WA x {}".format(b))
print("TLE x {}".format(c))
print("RE x {}".format(d))
