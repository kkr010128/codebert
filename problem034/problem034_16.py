x1,x2,x3,x4,x5,x6 = map(int,(input().split()))
n = int(input())
T=[]
for k in range(n):
    i,j = map(int, (input().split()))
    T.append([i,j])
L=[x1,x2,x3,x4,x5,x6]

for k in T:
    while L[0] != k[0]:
        L = [L[4], L[0], L[2], L[3], L[5], L[1]]
        if L[0] == k[0]:
            pass
        else:
            L = [L[3], L[1], L[0], L[5], L[4], L[2]]

    while L[1] != k[1]:
        L = [L[0], L[3], L[1], L[4], L[2], L[5]]
        if L[1] == k[1]:
            pass
        else:
            L = [L[0], L[3], L[1], L[4], L[2], L[5]]
    print(L[2])