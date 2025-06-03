#C - Count Order
#DFS
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

a = 0
b = 0
cnt = 0
def dfs(A):
    global cnt
    global a
    global b
    if len(A) == N:
        cnt += 1
        if A == P:
            a = cnt
        if A == Q:
            b = cnt
        return   
    for v in range(1,N+1):
        if v in A:
            continue
        A.append(v)
        dfs(A)
        A.pop()
dfs([])
print(abs(a-b))