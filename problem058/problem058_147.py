def a():
    data_set=[]
    while True:
        s=input().split()
        data_set.append(s)
        if ["0","0"] in data_set:
            break
    data_set=data_set[:-1]
    import itertools
    for i in data_set:
        count=0
        n=int(i[0])
        x=int(i[1])
        num=list(itertools.combinations(range(1,n+1),3))
        for j in num:
            if sum(j)==x:
                count+=1
        print(count)
a()
