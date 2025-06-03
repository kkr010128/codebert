n = int(input())
A = [int(input()) for i in range(n)]
cnt = 0
G = []
g = 0
while 3*g+1 <= n:
    G.append(3*g+1)
    g = 3*g+1
G.reverse()
m = len(G)

def InsertionSort(A, n, g=1):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i -g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

def ShellSort(A, n):    
    for i in range(m):
        InsertionSort(A, n, G[i])

ShellSort(A, n)

print(m)
print(*G)
print(cnt)  
print(*A, sep = "\n")
