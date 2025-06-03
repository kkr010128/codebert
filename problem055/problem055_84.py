l=[[[0 for i in range(10)]for j in range(3)]for k in range(4)]
s='#'*20
n=input()
for i in range(n):b,f,r,v=map(int,raw_input().split());l[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(-3,0):print ' '+' '.join(map(str,l[i][j]))
    if i<3:print s