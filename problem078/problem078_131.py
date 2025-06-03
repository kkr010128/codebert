s = int(input())

n = 10 ** s - 9 ** s - 9 ** s + 8 ** s

print(n % (10 ** 9 + 7))
