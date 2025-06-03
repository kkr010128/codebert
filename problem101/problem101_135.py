def main():
    r,g,b=map(int,input().split())
    k=int(input())
    while(k>0):
        if(g<=r):
            g=g<<1
            k-=1
        elif(b<=g):
            b=b<<1
            k-=1
        else:
            break;
    if(r<g and g<b):
        print('Yes')
    else:
        print('No')
    
main()
