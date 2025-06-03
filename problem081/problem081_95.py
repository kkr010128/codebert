list =input().split()

list = [int(i) for i in list]

D=list[0]

S=list[1]

T=list[2]


if(D/S<=T):
	print("Yes")
else:
	print("No")