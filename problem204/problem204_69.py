S=input()

Q=int(input())

inst=[]
for i in range(Q):
    array=input().split()
    inst.append(tuple(array))

rev=True
front_str=[]
back_str=[]
for i in range(Q):
    if int(inst[i][0])==1:
        rev=not rev
    elif rev:
        if int(inst[i][1])==1:
            front_str.append(inst[i][2])
        else:
             back_str.append(inst[i][2])
    else:
        if int(inst[i][1])==1:
            back_str.append(inst[i][2])
        else:
            front_str.append(inst[i][2])

if rev:
    front_str.reverse()
else:
    back_str.reverse()
    S=S[::-1]

front="".join(front_str)
back="".join(back_str)

if rev:
    print(front+S+back)
else:
    print(back+S+front)