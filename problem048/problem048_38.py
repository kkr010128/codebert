num = int(input())
data = list(map(int, input().split()))

data.sort()

min = data[0]
max = data[-1]
avg = 0

for tmp in data:
	avg += tmp

print(min,max,avg)
