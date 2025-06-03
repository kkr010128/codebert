n, a, b = list(map(int, input().split()))

whole = n // (a + b)
rest = n % (a + b)

blue = whole * a

if rest <= a:
	blue += rest
else:
	blue += a
	
print(blue)