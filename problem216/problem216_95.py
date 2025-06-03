arr = list(map(int, input().split()))
arr.sort()
if (arr[0] == arr[1]) and (arr[2] != arr[1]):
	print("Yes")
elif (arr[1] == arr[2]) and (arr[0] != arr[1]):
	print("Yes")
else:
	print("No")