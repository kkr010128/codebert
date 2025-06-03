from collections import Counter
def dis(i,j, x,y):
    return min(j-i, abs(x-i)+1+abs(j-y), abs(y-i)+1+(j-x))
n, x, y = map(int, input().split())
x,y = x-1,y-1
D = []
for i in range(n-1):
    for j in range(i+1, n):
        D.append(dis(i,j, x,y))
cD = Counter(D)
for i in range(1, n):
    print(cD[i])