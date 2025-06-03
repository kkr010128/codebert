import itertools
while 1:
    n,x=map(int,raw_input().split())
    if n==0 and x==0:
        break
    else:
        answer=0
        l=range(1,n+1)
        for ele in itertools.combinations(l,3):
            if sum(ele)==x:
                answer+=1
        print answer