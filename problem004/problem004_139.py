N = int(input())
for i in range(N):
	l = list(map(int,input().split()))
	l.sort()
	if l[0]*l[0]+l[1]*l[1] == l[2]*l[2]: print("YES")
	else: print("NO")