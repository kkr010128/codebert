l=[[[0 for i in range(10)] for i in range(3)] for i in range(4)]
n=int(input())
for i in range(n):
	a,b,c,d=list(map(int,input().split()))
	l[a-1][b-1][c-1]+=d
for i in l[:-1]:
	for j in i:
		print(" "+" ".join(list(map(str,j))))
	print("####################")

for j in l[-1]:
	print(" "+" ".join(list(map(str,j))))