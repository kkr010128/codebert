def f(a,b):
    if b:return f(b,a%b)
    p=set()
    for i in range(2,int(a**0.5)+1):
        while True:
            if a%i==0:
                a//=i
                p.add(i)
            else:
                break
    if a!=1:
        return len(p)+2
    return len(p)+1
print(f(*map(int,input().split())))