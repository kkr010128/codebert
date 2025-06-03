import math
N = int(input())
X = math.ceil(math.sqrt(N))
li = [0]*N
xyz = []
for i in range(X):
    for j in range(X-i):
        for k in range(X-i-j):
            xyz1 = [i+1,j+i+1,k+j+i+1]
            xyz1.sort()
            if i+1 == j+i+1 == k+j+i+1:xyz1.append(1)
            elif i+1 != j+i+1 and i+1 != k+j+i+1 and j+i+1 != k+j+i+1:xyz1.append(6)
            else:xyz1.append(3)
            xyz.append(xyz1)
xyz.sort()
for l in xyz:
    n = l[0]**2 + l[1]**2 + l[2]**2 + l[0]*l[1] + l[1]*l[2] + l[2]*l[0]
    try:
        li[n-1] += l[3]
    except:pass
for n in li[0:N:]:
    print(n)