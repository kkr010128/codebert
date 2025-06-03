def tripleDots(n, string):
	string_len = len(string)
	if string_len > n : 
		string = string[ 0 : n ] + "..."
	print(string)

arr = ["", ""]

for i in range(2):
	arr[i] = input()


tripleDots(int(arr[0]), arr[1])