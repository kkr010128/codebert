D=int(input())
c = [int(i) for i in input().split()]
s=[]
for i in range(D):
    s.append([int(j) for j in input().split()])
t=[0] * D
for i in range(D):
    t[i] = int(input())

tst = [0] * 26
last = [0] * 26
for i,j in enumerate(t):
    tst[j-1] += s[i][j-1]
    last[j-1] = i+1
    for k in range(26):
        if k != j-1:
            tst[k] -= (i+1 - last[k])*c[k] 
    print(sum(tst))

