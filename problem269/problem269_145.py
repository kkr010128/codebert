def main():
    t1,t2=map(int,input().split())
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    if t1*a1+t2*a2==t1*b1+t2*b2:
        return 'infinity'
    if a1<b1:
        a1,b1=b1,a1
        a2,b2=b2,a2
    if a2>b2:
        return 0
    d1=(a1-b1)*t1
    d2=(b2-a2)*t2
    if d1>d2:
        return 0
    d=d2-d1
    if d1%d==0:
        return d1//d*2
    return d1//d*2+1
    
if __name__=='__main__':
    print(main())