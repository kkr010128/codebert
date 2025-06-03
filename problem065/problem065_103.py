n=input()
count=0
while 1 :
    x=[i for i in input().split()]
    if x[0]=="END_OF_TEXT":
        break
    for i in range(len(x)):
        if x[i].lower()==n.lower():
            count=count+1
print(count)