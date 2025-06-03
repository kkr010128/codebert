a, b, c = [int(n) for n in input().split()]
d = c-a-b
if d < 0:
    print("No")
elif 4*a*b < d*d:
    print("Yes")
else:
    print("No")

#a + 2sqrt(ab) + b < c
#sqrt(4ab) < c-a-b
#4ab < d^2
