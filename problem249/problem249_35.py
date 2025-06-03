a,b,c = map(int,input().split())
if a>= c:
    print(a-c,b)
elif a+b<=c:
    print("0 0")
elif a < c and c < a+b:
    print("0",a+b-c)