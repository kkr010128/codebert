for i in range(int(input())):
    a,b,c=map(lambda x:int(x)**2,input().split())
    if a+b==c or b+c==a or c+a==b:
        print("YES")
    else:
        print("NO")
