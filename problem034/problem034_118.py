# your code goes here
#dice2
def np(dl,nu):
    l=0
    while dl[l]!=nu:
        l+=1
    return l
def si(n1,n2):
    if n1==1:
        if n2==2:
            return 3
        elif n2==3:
            return 5
        elif n2==4:
            return 2
        else:
            return 4
    elif n1==2:
        if n2==1:
            return 4
        elif n2==3:
            return 1
        elif n2==4:
            return 6
        else:
            return 3
    elif n1==3:
        if n2==2:
            return 6
        elif n2==5:
            return 1
        elif n2==1:
            return 2
        else:
            return 5
    elif n1==4:
        if n2==1:
            return 5
        elif n2==2:
            return 1
        elif n2==5:
            return 6
        else:
            return 2
    elif n1==5:
        if n2==1:
            return 3
        elif n2==3:
            return 6
        elif n2==4:
            return 1
        else:
            return 4
    elif n1==6:
        if n2==3:
            return 2
        elif n2==2:
            return 4
        elif n2==5:
            return 3
        else:
            return 5
D=[int(i) for i in input().split()]
q=int(input())
for i in range(q):
    n=[int(i) for i in input().split()]
 #   print(n)
    p=[]
    for j in range(2):
        p.append(np(D,n[j]))
  #  print(p)
    print(D[si(p[0]+1,p[1]+1)-1])