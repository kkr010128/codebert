num=int(input())
command=[input().split() for i in range(num)]
dic={}

for i in command:
    if i[0]=="insert":
        dic[i[1]]=1
    if i[0]=="find":
        if i[1] in dic:
            print("yes")
        else:
            print("no")
