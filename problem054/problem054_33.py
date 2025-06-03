
def check(mlist, s):
    if len(mlist) == 13:
        return 0
    else:
        lack = []
        for i in range(1, 14):
            if not i in mlist:
                lack.append(i)
                    
        #print(lack)
        for j in lack:
            print("{} {}".format(s, j))
        return 0


n = int(input())
Slist = []
Hlist = []
Clist = []
Dlist = []

for i in range(n):
    mark, num = input().split()
    num = int(num)

    if mark == 'S':
        Slist.append(num)
    elif mark == 'H':
        Hlist.append(num)
    elif mark == 'C':
        Clist.append(num)
    else:
        Dlist.append(num)
        
Slist.sort()
Hlist.sort()
Clist.sort()
Dlist.sort()
    
check(Slist, 'S')
check(Hlist, 'H')
check(Clist, 'C')
check(Dlist, 'D')
