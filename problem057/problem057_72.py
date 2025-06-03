m=f=r=0
while 1:
    m,f,r=map(int,input().split())
    x=m+f
    if m==f==r==-1:break
    elif m==-1 or f==-1 or x<30:print('F')
    elif x>=80:print('A')
    elif 65<=x<80:print('B')
    elif 50<=x<65 or r>=50:print('C')
    else:print('D')