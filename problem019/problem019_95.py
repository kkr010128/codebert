#16D8101014F 久留米 竜之介 Kurume Ryunosuke Python
All = 0
q = []
Queue = []
tmp,time = map(int,input().split())
for i in range(tmp):
    p,zi =input().split()
    q.append([p,int(zi)])
while len(q) > 0:
    if q[0][1]<= time:
        All+=q[0][1]
        v=q.pop(0)
        Queue.append([v[0],All])
    else:
        All+=time
        q[0][1]-=time
        last=q.pop(0)
        q.append(last)
for i in range(len(Queue)):
    print("{0} {1}".format(Queue[i][0],Queue[i][1]))
