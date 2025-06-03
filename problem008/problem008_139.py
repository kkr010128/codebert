def disc(s,d):
	ans[d][0] = s
	s += 1
	if main[d][0] != 0:
		for l in range(1,int(main[d][0])+1):
			if ans[int(main[d][l])-1][0] == 0:
				s = disc(int(s),int(main[d][l])-1)
	ans[d][1] = s
	return s+1

n = int(input())

main = []

for i in range(n):
	a = input().split()
	if int(a[1]) > 0:
		main.append(a[1:])
	else:
		main.append([0])

del a

ans = [[0] * 2 for i in range(n)]

ls = disc(1,0)
for i in range(n):
	if ans[i][0] == 0:
		ls = disc(int(ls),i)


for i in range(n):
	print(str(i+1) + " " + str(ans[i][0]) + " " + str(ans[i][1]))

