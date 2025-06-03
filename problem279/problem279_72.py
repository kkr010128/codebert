n=int(input())
s=input()
if n%2==1:
    print("No")
    exit()
half=n//2
if s[:half]==s[half:]:
    print("Yes")
else:
    print("No")
