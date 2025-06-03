n = int(input())
debt = 100000

for i in range(n):
	debt = debt * 1.05
	round = debt % 1000
	if round != 0:
		debt = (debt // 1000 + 1) * 1000

print(int(debt))