def get_ints():
	return map(int, input().split())
def get_list():
	return list(map(int, input().split()))

l, r, d = get_ints()
c = 0
for i in range(l, r + 1):
	if i % d == 0:
		c += 1
print(c)