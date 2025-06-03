r,c=map(int,raw_input().split())
A=[]
for i in range(r):
    A.append(map(int,raw_input().split()))
    A[i].append(sum(A[i]))
A.append([sum([A[i][j] for i in range(r)]) for j in range(c+1)])
for i in range(r+1):
    print(' '.join(map(str,A[i])))