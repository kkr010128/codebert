l = list(map(int,input().split()))
#print(l)

if l[0]==l[1]!=l[2]:
    print('Yes')
elif l[0]!=l[1]==l[2]:
    print('Yes')
elif l[0]==l[2]!=l[1]:
    print('Yes')
else:
    print('No')