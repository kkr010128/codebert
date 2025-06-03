N = int(input())
a = list(map(int, input().split()))

b = []
j = N-1

while j > 0:
	print("{} ".format(a[j]),end = "")
	j -= 1
print(a[j])