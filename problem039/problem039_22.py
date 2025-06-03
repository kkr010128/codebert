tmp = input()
tmp = tmp.split(" ")
tmp = list(map(int,tmp))
if tmp[0] < tmp[1] and tmp[1] < tmp[2]:
	print("Yes")

else :
	print("No")