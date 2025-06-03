nums = input()
a,b,c = nums.split(' ')
nd = 0

for i in range(int(a),int(b)+1):
	if int(c)%i == 0:
		nd = nd + 1

print(nd)
