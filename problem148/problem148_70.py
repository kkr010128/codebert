a,b,c,k = (int(a) for a in input().split())
if a >= k :
    print(k)
elif  a+b >= k :
    print(a)
else :
    print(a - min(c,(k-(a+b))))