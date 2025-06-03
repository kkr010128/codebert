n,m = map(int,input().split())
rule = [list(map(int,input().split())) for i in range(m)]
jj = 0
if n == 1:
    for i in range(0,10**n):
        jud = 0
        for j in range(m):
            if int(str(i)[rule[j][0]-1]) != rule[j][1]:
                jud =1
        if jud == 0:
            print(i)
            jj = 1
            break
else:
    for i in range(10**(n-1),10**n):
        jud = 0
        for j in range(m):
            if int(str(i)[rule[j][0]-1]) != rule[j][1]:
                jud =1
        if jud == 0:
            print(i)
            jj = 1
            break
if jj == 0:
    print(-1)
