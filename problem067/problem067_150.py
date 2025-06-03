n = int(input())
taro = 0
hanako = 0

for i in range(n):
	animals = input().split()
	taro_animal = animals[0]
	hanako_animal = animals[1]
	if taro_animal > hanako_animal:
		taro += 3
	elif taro_animal < hanako_animal:
		hanako +=3
	else:
		taro += 1
		hanako += 1

print(taro, hanako)