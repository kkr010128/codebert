a,b,c=map(int,input().split())
if a+b>=c:
    print("No")
    exit()
print("Yes" if 4*a*b<(c-b-a)**2 else "No")
    
