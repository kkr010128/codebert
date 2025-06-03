#ITP1_11-B Dice 2
rep=[
    [1,2,4,3,1],
    [2,0,3,5,2],
    [0,1,5,4,0],
    [0,4,5,1,0],
    [0,2,5,3,0],
    [1,3,4,2,1]
]
d = input().split(" ")
q = int(input())
dic={}
for i in range(6):
    dic.update({d[i]:i})
for i in range(q):
    a,b = input().split(" ")
    for j in range(4):
        top=dic[a]
        front = dic[b]
        if(d[rep[top][j]]==d[front]):
            print(d[rep[top][j+1]])