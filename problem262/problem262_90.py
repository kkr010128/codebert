n=int(input())
ev=[]
for i in range(n):
    a=int(input())
    ev.append([list(map(int,input().split())) for _ in range(a)])
ans=0
for i in range(2**n):
    bit=(bin(i)[2:].zfill(n))
    flag=1
    for j in range(n):
        if bit[j]=="0":
            continue
        for e in ev[j]:
            if int(bit[e[0]-1])!=e[1]:
                flag=0
    if flag:
        ans=max(ans,bit.count("1"))
print(ans)