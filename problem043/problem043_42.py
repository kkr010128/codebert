while 1:
    x,y=map(int,raw_input().split())
    if x==y==0: exit()
    else: print min(x,y),max(x,y)