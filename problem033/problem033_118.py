

u, s, e, w, n, b = map(int, input().split())
roll = input()
for i in roll:
    if i == "E":
        e,u,w,b = u,w,b,e
    elif i == "S":
        s,u,n,b = u,n,b,s
    elif i == "W":
        w,u,e,b = u,e,b,w
    elif i == "N":
        n,u,s,b = u,s,b,n
print(u)