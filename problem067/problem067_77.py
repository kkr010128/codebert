n=int(input())
pointx=0
pointy=0
for i in range(n):
    x,y=[j for j in input().split()]
    p=1
    if len(x)<len(y):
        for j in range(len(x)):
            if ord(list(x)[j])>ord(list(y)[j]):
                pointx=pointx+3
                p=0
                break
            elif ord(list(x)[j])<ord(list(y)[j]):
                pointy=pointy+3
                p=0
                break
        if p:
            pointy=pointy+3
    elif len(x)==len(y):
        for j in range(len(x)):
            if ord(list(x)[j])>ord(list(y)[j]):
                pointx=pointx+3
                p=0
                break
            elif ord(list(x)[j])<ord(list(y)[j]):
                pointy=pointy+3
                p=0
                break
        if p:
            pointx=pointx+1
            pointy=pointy+1
    else:
        for j in range(len(y)):
            if ord(list(x)[j])>ord(list(y)[j]):
                pointx=pointx+3
                p=0
                break
            elif ord(list(x)[j])<ord(list(y)[j]):
                pointy=pointy+3
                p=0
                break
        if p:
            pointx=pointx+3
print("{0} {1}".format(pointx,pointy))