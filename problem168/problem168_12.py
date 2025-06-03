N,M = map(int,input().split())
L = map(int,input().split())
work = 0
for i in L :
    work += i
if N >= work :
    print ( N - work )
else :
    print ("-1")