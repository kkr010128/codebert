s = list(str(input()))
q = int(input())
o = ['']*q
for i in range(q):
    o[i] = str(input())
    
for i in range(q):
    order = o[i].split(' ')
    if order[0] == 'print':
        a,b = int(order[1]),int(order[2])
        for i in range(a,b+1):
            print(s[i],end = '')
        print('')

    elif order[0] == 'reverse':
        a,b = int(order[1]),int(order[2])
        tmp = s[a:b+1]
        tmp.reverse()
        s[a:b+1] = tmp        
        
    elif order[0] == 'replace':
        a,b,p = int(order[1]),int(order[2]),list(order[3])
        for i in range(b-a+1):
            s[a+i] = p[i]