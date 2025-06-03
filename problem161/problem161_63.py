a, b, n = map(int, input().split())

c = min(b - 1, n)
#logging.debug(c)
print(int(((a * c) / b) // 1 - (a * ((c / b) // 1))))