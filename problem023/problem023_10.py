n=int(input())
list={}
list1=[]
for i in range(n):
    a,b=map(str,input().split())
    if a=="insert":
        list.setdefault(b,i)
    if a=="find":
        if b in list:
            list1.append("yes")
        else:
            list1.append("no")

for i in list1:
    print(i)
