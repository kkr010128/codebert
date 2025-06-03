s=input()
n=len(s)
if n%2==1:
    print("No")
    exit()
for i in range(n-1):
    if s[i]=="h":
        if s[i+1]!="i":
            print("No")
            exit()
    elif s[i]=="i":
        if s[i+1]!="h":
            print("No")
            exit()
    else:
        print("No")
        exit()
print("Yes")