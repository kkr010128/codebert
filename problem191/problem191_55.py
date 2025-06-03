n = int(input())
a = n//3
b = n%3

if b == 1:
    print((a+1/3)**3)
elif b==2:
    print((a+2/3)**3)
else:
    print(a**3)