a,b,c,d=map(int,input().split())
def ret(a,b,c,d):
    return max(b*d,a*c,0 if (a*b<=0 or c*d<=0) else -1e64,a*d,b*c)
print(ret(a,b,c,d))