import math

n = int(input())
address = list(map(int, input().split()))

min_hp = math.inf

for i in range(1, 101):
	hp = sum(map(lambda x: (x - i) ** 2, address))
	if hp < min_hp:
		min_hp = hp
		
print(min_hp)