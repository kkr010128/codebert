count=0
answer=[]
while count<50:
    m,f,r=(int(x) for x in input().split())
    if m==-1 and f==-1 and r==-1:
        break
    if m==-1 or f==-1:
        answer.append('F')
    elif m+f>=80:
        answer.append('A')
    elif 65<=m+f<80:
        answer.append('B')
    elif 50<=m+f<65:
        answer.append('C')
    elif 30<=m+f<50:
        if r>=50:
            answer.append('C')
        else:
            answer.append('D')
    else:
        answer.append('F')
    count+=1
for i in answer:
    print(i)
