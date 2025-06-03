def solve():
    v=list(map(int,input().split()))
    a=v[0]
    b=v[1]
    c=v[2]
    if c <= a + b:
        return False
    return 4 * a * b < (c - a - b)**2

if solve():
    print("Yes")
else:
    print("No")