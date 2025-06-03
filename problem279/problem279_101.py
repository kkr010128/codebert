n = int(input())
s = input()
if n%2==1:
    print("No") 
else:
    s1 = ""
    s2 = ""
    for i in range(0, n//2):
        s1+=s[i]
        s2+=s[n//2 + i]
    if(s1 == s2):
        print("Yes")
    else:
        print("No")
