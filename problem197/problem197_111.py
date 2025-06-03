a, b, c=map(int, input().split())
left=(a+b-c)**2
right=4*a*b
print("Yes") if a+b<c and left> right else print("No")