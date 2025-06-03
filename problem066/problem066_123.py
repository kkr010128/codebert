b=[]
i=-1
while True:
    a=input()
    if a=="-":
        break
    else:
        b.append(a)
        i+=1
        c=int(input())
        for j in range(c):
            a=int(input())
            d=b[i][a:]
            b[i]=b[i][0:a]
            b[i]=d+b[i]
for i in b:
    print(i)
