n = int(input())
E = [[]]*n

for i in range(n):
    inputs = list(map(int, input().split()))
    if inputs[1]==0:
        continue
    else:
        for j in inputs[2:]:
            E[i] = E[i] + [j-1]

beg = [-1]*n
fin = [-1]*n  

t = 0      
def f(i):
    global t
    #print(i,t)
    t += 1
    beg[i] = t
    for c in E[i]:
        if beg[c]>0:
            continue
        else:
            f(c)
    t+=1
    fin[i] = t
    

for i in range(n):
    if beg[i]<0:
        f(i)
for i in range(n):
    print(i+1, beg[i], fin[i])
