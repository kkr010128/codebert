def isPrime(num):
	if num <= 1:
		return False

	elif num == 2 or num == 3:
		return True

	elif num % 2 == 0:
		return False

	else:
		count = 3

		while True:
			if num % count and count ** 2 <= num:
				count += 2
				continue

			elif num % count == 0:
				return False

			else:
				break

		return True


if __name__ == '__main__':
	count = 0
	N = int(input())
	
	for i in range(N):
		i = int(input())

		if isPrime(i):
			count += 1

	print(count)

