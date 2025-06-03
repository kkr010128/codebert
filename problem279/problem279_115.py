import sys
n=int(input())
s=input()
if n%2==1:
    print("No")
    sys.exit()
else:
    s1=s[:n//2]
    s2=s[n//2:]
    # print(s1,s2)
    if s1==s2:
        print("Yes")
    else:
        print("No")