_ = input()
arr = list(map(int, input().split()))

min = arr[0]
max = arr[0]
sum = 0

for a in arr:
	if a < min:
		min = a
	if max < a:
		max = a
	sum += a

print(min, max, sum)