a = []
while True:
    d = list(map(int,input().split()))
    if d == [-1,-1,-1]:
        break
    a.append(d)

def Point2Grade(d):
    m,f,r = d
    if (m==-1)|(f==-1):
        return 'F'
    elif m+f >= 80:
        return 'A'
    elif m+f >= 65:
        return 'B'
    elif m+f >= 50:
        return 'C'
    elif m+f >= 30:
        if r >=50: return 'C'
        else: return 'D'
    else: return 'F'

for x in a:
    print(Point2Grade(x))