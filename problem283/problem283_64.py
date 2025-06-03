n = int(input())

if n-2 == 0:
    print(0)
elif n%2 == 0:
    if n != 3:
        print(int(n/2)-1)
    else:
        print(1)
else:
    print(int(n/2))
