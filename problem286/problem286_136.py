a,b = input().split()

a=int(a)
b=int(b)

if a>=1 and a<=9 and b>=1 and b<=9:
    print(a*b)
else: print("-1")