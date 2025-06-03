S = input().strip()
Q = int(input())
ind = 1
x = []
y = []
for i in range(Q):
    q = list(input().split())
    if len(q)==1:
        ind = ind*(-1)
    else:
        if q[1]=="1":
            if ind>0:
                x.append(q[2])
            else:
                y.append(q[2])
        else:
            if ind>0:
                y.append(q[2])
            else:
                x.append(q[2])
if ind>0:
    x = x[::-1]
    S = "".join(x)+S+"".join(y)
else:
    S = S[::-1]
    y = y[::-1]
    S = "".join(y)+S+"".join(x)
print(S)