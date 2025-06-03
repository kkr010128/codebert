n=int(input())
a=[]
while n>26:
    n=n-1
    a.append(chr(ord('a') + n%26))
    n=n//26

n=n-1
a.append(chr(ord('a') + n%26))
a.reverse()
print("".join(a))
