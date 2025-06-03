s=input()
n=len(s)
if n%2==1:
    print("No")
elif "hi"*(n//2)==s:
    print("Yes")
else:
    print("No")