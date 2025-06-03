n,t = map(int, input().split())
Task=[]
for i in range(n):
    nm,le= map(str, input().split())
    Task.append([nm,le])
T=0
while n >0:
    k = Task.pop(0)
    k[1]=int(k[1])
    if k[1] > t:
        k[1]=k[1]-t
        T=T+t
        Task.append(k)
        n = len(Task)
    else:
        T=T+k[1]
        k[1]=T
        print(' '.join(map(str, k)))
        n = len(Task)