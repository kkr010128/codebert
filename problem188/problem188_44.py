apple = list(map(int, input().split()))
x = apple[0]
y = apple[1]        #to eat
a = apple[2]
b = apple[3]        #i have
c = apple[4]

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

XredApl = []
for i in range(x):
    XredApl.append(p[i])

YgrnApl = []
for i in range(y):
    YgrnApl.append(q[i])
    
fnlst = XredApl + YgrnApl + r 
fnlst.sort(reverse=True)
s = 0
for i in range(x+y):
    s += fnlst[i]
    
print(s)
