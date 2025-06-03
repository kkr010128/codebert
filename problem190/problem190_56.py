s = input()
n = len(s)
n1 = (n-1)//2
n2 = (n+1)//2
 
if s == s[::-1]:
    if s[:n1] == s[n2:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")