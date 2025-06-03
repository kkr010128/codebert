s=list(input())
n=len(s)
if list(s[::-1])==list(s[:]) and list(s[(n-1)//2-1::-1])==list(s[:(n-1)//2]) and list(s[:(n+3)//2-2:-1])==list(s[(n+3)//2-1:]):
    print("Yes")
else:
    print("No")