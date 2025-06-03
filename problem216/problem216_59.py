a,b,c = (int(a) for a in input().split())
if a == b == c or (a != b and b != c and c != a) :
    print("No")
else : print("Yes")