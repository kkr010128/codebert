a=input()
b=input()
if(a==b[0:len(b)-1] and len(b)-len(a)==1):
    print('Yes')
else:
    print('No')