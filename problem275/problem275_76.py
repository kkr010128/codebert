res = {1:300000, 2:200000, 3:100000}
a, b = map(int, input().split())
if a == b == 1:
	c = 400000
else:
	c = 0
try:
	a = res[a]
except:
	a = 0
try:
	b = res[b]
except:
	b = 0
print(c+a+b)