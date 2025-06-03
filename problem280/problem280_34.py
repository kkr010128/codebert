import itertools as it

n = int(input())
lst = []
for i in range(n):
	x, y = list(map(int, input().split()))
	lst.append([x, y])
perm = list(it.permutations(lst))

cost = []
for i in perm:
	temp = 0
	for j in range(len(i)-1):
		temp += (((i[j][0] - i[j+1][0])**2) + ((i[j][1] - i[j+1][1])**2))**0.5
	cost.append(temp)

print(sum(cost) / len(cost))