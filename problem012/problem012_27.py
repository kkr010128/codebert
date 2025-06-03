# coding: utf-8
from math import sqrt

def isPrime(n):
	if n == 2:
		return True
	elif n < 2 or n % 2 == 0:
		return False
	else:
		i = 3
		while i <= sqrt(n):
			if n % i == 0:
				return False
			i += 2
		return True

def main():
	n = input()
	print sum([1 if isPrime(x) else 0 for x in [input() for _ in xrange(n)]])

if __name__ == '__main__':
	main()