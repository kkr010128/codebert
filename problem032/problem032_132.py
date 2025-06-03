import math

n = int(raw_input())
x = map(int, raw_input().split())
y = map(int, raw_input().split())

for i in range(3):
	sum = 0
	for j in range(n):
		sum += (math.fabs(x[j] - y[j]))**(i+1)
		#print("sum = {:}".format(sum))
	ans = sum ** (1.0/(i+1))
	print("{:.6f}".format(ans))

ans = 0
for i in range(n):
	if math.fabs(x[i] - y[i]) > ans:
		ans = math.fabs(x[i] - y[i])
print("{:.6f}".format(ans))