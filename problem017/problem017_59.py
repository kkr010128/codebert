def InsertSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt
        
def ShellSort(A, n):
    cnt = 0
    G = [1]
    h = G[0]
    while True:
        h = h*3 + 1
        if h > n:
            break
        G.append(h)
    print(len(G))
    print(' '.join(reversed(list(map(str, G)))))
    for h in reversed(G):
        cnt = InsertSort(A, n, h, cnt)
    print(cnt)
            
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
    
ShellSort(A, n)

for num in A:
    print(num)
