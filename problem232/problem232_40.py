a,b=map(int,input().split())
a1=f"{a}"*b
b1=f"{b}"*a
print(a1 if a1<b1 else b1)