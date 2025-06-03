s,t=map(str,input().split())
a,b=map(int,input().split())
u=input()
if u==s:
    print("{0} {1}".format(a-1,b))
else:
    print("{0} {1}".format(a,b-1))