n=int(input())
s=list(input())
if n%2==1:
    print("No")
elif s[:n//2]==s[n//2:n]:
    print("Yes")
else:
    print("No")
