while(1):
	char_list = list(input())
	int_list = [0 for i in range(len(char_list))]

	if char_list[0] == '0':
		break
	for i in range(len(char_list)):
		int_list[i] = int(char_list[i])
	print(sum(int_list))