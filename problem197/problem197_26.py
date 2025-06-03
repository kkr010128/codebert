a, b, c = map(int, input().split())
if a*a + b*b + c*c -2*(a*b + b*c + c*a) > 0 and c-a-b > 0:
    print("Yes")
else:
    print("No")