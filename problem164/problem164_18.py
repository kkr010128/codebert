a, b, c, d = map(int, input().split())
if c%b==0:
    x = c//b
else:
    x = c//b+1
if a%d==0:
    y = a//d
else:
    y = a//d+1
    
if x<=y:
    print("Yes")
else:
    print("No")