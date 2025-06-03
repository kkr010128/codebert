import itertools

n = int(input())
a = list()
for i in range(1,n+1):
    a.append(i)
b = list(input().split())
c = list(input().split())
for i in range(0,n):
    b[i]=int(b[i])
    c[i]=int(c[i])
cnt = 1
for i in itertools.permutations(a):
    #print(i)
    if(tuple(b)==i):
        cnta = cnt
        #print('p is '+str(cnta))
    if(tuple(c)==i):
        cntb = cnt
        #print('q is '+str(cntb))
    cnt +=1
print(abs(cnta-cntb))
