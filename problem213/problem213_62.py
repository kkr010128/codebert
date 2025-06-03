import sys
N = int(input())
X = [int(c) for c in input().split()]
l = [10**10]
for i in range(1,101):
    l.append(0)
    for j in range(len(X)):
        l[i] += (X[j]-i)**2
    
    if l[i-1] < l[i]:
        print(l[i-1])
        sys.exit(0)