while True:
	chk_list = input()

	if chk_list == "-":
		break

	num = int(input())
	for i in range(num):
		n = int(input())
		chk_list = chk_list[n:] + chk_list[0:n]
	print(chk_list)

