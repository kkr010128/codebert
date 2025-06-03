def max(a):
	max = -10000000
	for i in a:
		if max < i:
			max = i
	return max

def min(a):
	min = 10000000
	for i in a:
		if min > i:
			min = i
	return min

def sum(a):
	sum = 0
	for i in a:
		sum += i
	return sum


input()
a = list(map(int, input().split()))

print(min(a), max(a), sum(a))