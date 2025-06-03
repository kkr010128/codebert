import math

a, b, c = list(map(int, input().split()))

if a+b > c:
    print("No")

elif 4*a*b  < (c-a-b)**2:
    print("Yes")
else:
    print("No")