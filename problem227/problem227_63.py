N,A=map(int,input().split())
B=sorted(list(map(int,input().split())))
for j in range(A):
    if B!=[]: B.pop()
print(sum(B))