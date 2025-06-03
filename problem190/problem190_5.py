s = input()

n = len(s)
for i in range(n//2):
    if s[i]!=s[n-i-1] :
        print("No")
        exit()

n1 = (n-1)//2
for i in range(n1//2):
    if s[i]!=s[n1-i-1] :
        print("No")
        exit()

n2 = (n+3)//2
for i in range(n-n2):
    if s[i]!=s[n-i-1] :
        print("No")
        exit()

print("Yes")