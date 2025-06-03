n = int(input())
a = []
for i in range(n):
	s,t = map(str, input().split())
	t = int(t)
	a.append([s,t])
x = input()
a.reverse()
ss = 0
for i in range(n):
	if a[i][0] == x:
		print (ss)
		exit()
	ss += a[i][1]
print (ss)
