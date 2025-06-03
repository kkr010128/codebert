a,b,c = map(int, raw_input().split())
t = 0
for n in range(a,b+1):
 if c%n == 0:
 	t += 1
print str(t)