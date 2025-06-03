a, b = input().split()

a = int(a)

b = round(100*float(b))

ans = a*b

print(int(ans//100))