num = int(input())
data = list(map(int, input().split()))

min = data[0]
max = data[0]
avg = 0

for tmp in data:
	if tmp < min:
		min = tmp
	if tmp > max:
		max = tmp
	avg += tmp

print(min,max,avg)
