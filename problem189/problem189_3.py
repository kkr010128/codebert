a = input().split()
b = int(a[0])
c = int(a[1])
if b == 1 and c == 1:
    print(0)
elif b>=2 and c>=2:
    d = b-1
    e = c-1
    f = b*d/2
    g = c*e/2
    print(int(f+g))
elif b<=1 and c>=2:
    d = c-1
    f = c*d/2
    print(int(f))
elif b>=2 and c<=1:
    d = b-1
    f = b*d/2
    print(int(f))