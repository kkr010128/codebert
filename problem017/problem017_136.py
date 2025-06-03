import copy as cp

n = int(input())
A = list()
for i in range(n):
    A.append(int(input()))

count = 0
#print(A)
def insertionsort(A,n,g):
    global count
    for i in range(g,n):
        v = A[i]
        j = i-g
        while (j >= 0 and A[j] > v):
            A[j+g] = A[j]
            A[j] = v
            j = j - g
            v = A[j+g]
            count += 1

#decision of m and g
G = list()
G.append(int(1))
i = 0
while (G[i] <= n):
    G.append(3*G[i] + 1)
    i += 1
del G[-1]
G.reverse()
m = len(G)
#print(G,m)


#shellsort

for i in range(m):
    insertionsort(A,n,G[i])

#output
print(m)
for k in range(m-1):
    print(str(G[k])+" ",end = "")
print(str(G[m-1]))
print(count)
for k in range(n):
    print(str(A[k]))

