n,m=map(int,input().split())
ans=[0]*n
num1=[[] for _ in range(n)]
def ap(num01,num02):
    num1[num01-1].append(num02)
    num1[num02-1].append(num01)
for i in range(m):
    a,b=map(int,input().split())
    ap(a,b)
queue=[1]
def apq(num01):
    queue.append(num01)
def qp():
    return queue.pop(0)
for i in range(n):
    if len(queue)==0:
        break
    num=qp()
    for j in range(len(num1[num-1])):
        if ans[num1[num-1][j]-1]==0:
            apq(num1[num-1][j])
            ans[num1[num-1][j]-1]=num
if ans.count(0)!=0:
    print("No")
else:
    print("Yes")
    for i in range(1,n):
        print(ans[i])
