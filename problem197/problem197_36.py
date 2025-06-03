a, b, c = map(int, input().split())
if (a**2 + b**2 + c**2) > 2*(a*b + a*c + b*c) and (c - a -b) >= 0:print('Yes')
else:print('No')