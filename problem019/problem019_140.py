
import collections
#データの入力
a=input().split()

number=int(a[0])
quantum=int(a[1])

#保持データの作成
time=0

#キューの作成
name=[]
name=collections.deque()
q=[]
q=collections.deque()

#結果の保持
result=[[0 for i in range(2)]for j in range(number)]
endednumber=0

totaltime=0

for i in range(number):
    b=input().split()
    name.append(b[0])
    q.append(int(b[1]))
    totaltime+=int(b[1])

#キューの処理
while totaltime>time:
    cn=name.popleft()
    cq=q.popleft()

    if cq<=quantum:
        time+=cq

        result[endednumber][0]=cn
        result[endednumber][1]=time
        endednumber+=1
    else :
        time+=quantum
        newq=cq-quantum
        name.append(cn)
        q.append(newq)

#結果の表示
for i in range(number):
    print(result[i][0],result[i][1])





