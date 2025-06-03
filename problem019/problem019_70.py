n,q=map(int,input().split())
#print(n,p)
round_robin=[]
for i in range(n):
    x=input().split()
    name=x[0]
    t=int(x[1])
    round_robin.append([name,t])
#print(round_robin)
finished=[]
counter=0
while round_robin:
    left_time=round_robin[0][1]
    if left_time<=q:
        counter+=left_time
        finished.append([round_robin[0][0],counter])
        del round_robin[0]
    else:
        counter+=q
        left_time-=q
        round_robin[0]=[round_robin[0][0],left_time]
        round_robin.append(round_robin.pop(0))

for i in finished:
    print(*i)