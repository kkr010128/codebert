a, b, c, = map(int, input().split())
if 4*a*b < a*a + b*b + c*c + 2*a*b - 2*c*b - 2*c*a and 0 < c - (a + b):
    print("Yes") 

else:
    print("No")