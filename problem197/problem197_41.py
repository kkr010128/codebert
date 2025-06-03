a, b, c = map(int, input().split())
print("No" if c-a-b < 0 or 4*a*b >= (c-a-b)**2 else "Yes")
