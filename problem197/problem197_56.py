a, b, c = map(int, input().split())
if c - (a+b) < 0:
    print("No")
    exit()
if 4*a*b < c**2 - 2*c*(a+b) + (a+b)**2:
    print("Yes")
else:
    print("No")
