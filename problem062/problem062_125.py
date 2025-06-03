a=0

while True:
    z=str(input())
    if z == '0' :
        break
    for i in z:
        k=int(i)
        a+=k
    print(a)
    a=0