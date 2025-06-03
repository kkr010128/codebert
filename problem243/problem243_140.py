n=int(input())
box1=[]
box2=[]
for i in range(n):
    i=input().rstrip().split(" ")
    box1.append(i[0])
    box2.append(int(i[1]))
num=box1.index(input())
del box2[:num+1]
print(sum(box2))