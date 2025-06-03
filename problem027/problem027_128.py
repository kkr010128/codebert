n = int(input())
L = [[0,0],[100,0]]
for i in range(n):
    sub = []
    for j in range(len(L)-1):
        K = []
        a = L[j][0]
        b = L[j][1]
        c = L[j+1][0]
        d = L[j+1][1]
        if a == 0:
            K.append([a,b])
        K.append([a+((c-a)/3),b+((d-b)/3)])
        K.append([(a+c)/2+(b-d)*(3**0.5)/6,(b+d)/2+(c-a)*(3**0.5)/6])
        K.append([a+((c-a)*2/3),b+((d-b)*2/3)])
        K.append([c,d])
        sub = sub+K
    L = sub
for i in range(len(L)):
    print(L[i][0],L[i][1])
