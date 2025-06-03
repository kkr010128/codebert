n=int(raw_input())
p=[0,0]
for i in range(n):
        c=[0 for i in range(100)]
        c=map(list,raw_input().split())
        m=0
        while 1:
                try:
                        if c[0]==c[1]:
                                p[0]+=1
                                p[1]+=1
                                break
                        elif c[0][m]<c[1][m]:
                                p[1]+=3
                                break
                        elif c[1][m]<c[0][m]:
                                p[0]+=3
                                break
                        m+=1
                except IndexError:
                        if len(c[0])<len(c[1]):
                                p[1]+=3
                                break
                        if len(c[1])<len(c[0]):
                                p[0]+=3
                                break
print p[0], p[1]