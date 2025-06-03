a, b, c = list(map(int, input().split()))
frag1 = ((a+b-c)**2 -4*a*b) > 0
frag2 = a+b-c < 0
if  frag1 and frag2:
    print("Yes")
else:
    print("No")
