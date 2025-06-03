n=int(input())
if n%10==7:
    print("Yes")
    exit()
n//=10
if n%10==7:
    print("Yes")
    exit()
n//=10
if n%10==7:
    print("Yes")
    exit()
print("No")