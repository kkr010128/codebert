x = input().split()
a,b,c = int(x[0]), int(x[1]), int(x[2])
if a==b and a!=c:
    print("Yes")
elif a==c and a!=b:
    print("Yes")
elif b==c and b!=a:
    print("Yes")
else:
    print("No")