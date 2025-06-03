import collections

n,m = list(map(int,input().split()))

coriddorList = [set() for i in range(n+1)]
deepList = [-1 for i in range(n+1)]


for i in range(m):
    a,b = list(map(int,input().split()))
    coriddorList[a].add(b)
    coriddorList[b].add(a)

checkList = [0] * (n + 1)
ansList = [0] * (n + 1)
checkList[1] = 1
q = collections.deque()
q.appendleft(1)

while len(q) > 0:
    value = q.pop()
    for k in coriddorList[value]:
        if checkList[k] == 0:
            checkList[k] = 1
            ansList[k] = value
            q.appendleft(k)

print("Yes")
for i in range(2,n+1):
    print(ansList[i])