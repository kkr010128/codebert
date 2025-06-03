n = int(input())
mode = 0
memo = 0
for i in range(n):
	a,b = map(int,input().split())
	if a == b:
		memo += 1
	else:
		memo = 0
	if memo == 3:
		mode = 1
		break
if mode:
	print("Yes")
else:
	print("No")