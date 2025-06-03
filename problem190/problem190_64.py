def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

s=input()
n=len(s)
a=s[:n//2]
b=s[n//2 +1 : ]
if s==s[::-1] and a==a[::-1] and b==b[::-1]:
    print("Yes")
else:
    print("No")