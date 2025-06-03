s,t = map(int,input().split())
k,l = map(int,input().split())
m,n = map(int,input().split())
a = (k-m)*s
b = (l-n)*t

if a+b == 0:
    print("infinity")
elif a>0 and a+b>0:
    print(0)
elif a<0 and a+b<0:
    print(0)
else:
    div = abs(a) // abs(a+b)
    if div == abs(a) / abs(a+b):
        print(div*2)
    else:
        print(div*2+1)