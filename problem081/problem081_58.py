input_data  = list(map(int,input().split()))
time = input_data[0]  /  input_data[2]
if time > input_data[1]:
	print('No')
else:
	print('Yes')
