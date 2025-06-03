a,b,c = map(int,input().split())
if a > b:
    b,a = a,b
    if b > c:
        b,c = c,b
        if a > b:
            b,a = a,b
else:
    if b > c:
        b,c = c,b
        if a > b:
            b,a = a,b
            
print(f"{a} {b} {c}")
