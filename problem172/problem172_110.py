N =input()

flag = 0
for i in range(len(N)):
	if N[i] == "7":
		flag = 1
		break

if flag == 1:
	print("Yes")
else:
	print("No")