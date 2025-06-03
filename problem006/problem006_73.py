def main():
	from math import ceil

	debt = 100000
	n = int(input())

	for _ in range(n):
		debt *= 1.05
		debt = ceil(debt/1000)*1000

	print(debt)


if __name__ == '__main__':
	main()