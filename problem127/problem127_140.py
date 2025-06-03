X,Y= map(int,input().split())
a = Y/2-X 
b = X*2-Y/2

if Y%2 ==0:
    if a >= 0 and b >= 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')