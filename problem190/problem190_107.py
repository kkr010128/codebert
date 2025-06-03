s=input()
si=s[::-1]
a=s[:(len(s)-1)//2]
b=s[(len(s)+1)//2:]
if s == si :
    if a == a[::-1] and b == b[::-1]:
        print(("Yes"))
        exit()
print("No")