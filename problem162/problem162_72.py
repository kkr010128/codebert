n,m = map(int,input().split())
if m%2 == 1:
    a = 1
    b = a+2*(m//2)+2
    for i in range(m//2+1):
        print(a,a+2*(m//2-i)+1)
        a += 1
    for i in range(m//2):
        print(b,b+2*(m//2-i))
        b += 1
else:
    a = 1
    b = a+2*(m//2)+1
    for i in range(m//2):
        print(a,a+2*(m//2-i))
        a += 1
    for i in range(m//2):
        print(b,b+2*(m//2-i-1)+1)
        b += 1