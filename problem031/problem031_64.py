n=int(input())
while n!=0:
    S=0
    #print(n)
    l=input().rstrip().split()
    l=list(map(int,l))
    #print(l)
    m=sum(l)/len(l)
    #print(m)
    for i in range(len(l)):
        S+=(l[i]-m)**2
    print((S/len(l))**(1/2))
    n=int(input())
