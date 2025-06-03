N=input()
I=list(map(int,input().split()))
E=list(filter(lambda x:x%2==0,I))
if len(E)==0:
    print('APPROVED')
else:
    O=list(filter(lambda r:r%3!=0 and r%5!=0,E))
    if len(O)==0:
        print('APPROVED')
    else:
        print('DENIED')