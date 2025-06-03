n=int(input())
s=input()

if n==1:
    print("No")
else:
    h = int(n/2)
    a = s[0:h]
    b = s[h:]
    if a == b:
        print("Yes")
    else:
        print("No")