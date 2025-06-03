h,w,y=map(int,input().split())
c=[input() for _ in range(h)]
black=0
for i in range(h):
    for j in range(w):
        if c[i][j]=="#":
            black+=1
if black<y:
    print("0")
    exit()
hb=[]
wb=[]
for i in range(h):
    hb.append(c[i].count("#"))
for i in range(w):
    count=0
    for j in range(h):
        if c[j][i]=="#":
            count+=1
    wb.append(count)
bit=[]
for i in range(2**(h+w)): #行：[:h]、列：[h+1:]
    bit.append(bin(i)[2:].zfill(h+w))
ans=0
for i in bit:
    x=black
    for j in range(h):
        if i[j]=="1":
            for k in range(w):
                if i[h+k]=="1" and c[j][k]=="#":
                    x+=1
    for j in range(h):
        if i[j]=="1":
            x-=hb[j]
    for j in range(w):
        if i[h+j]=="1":
            x-=wb[j]
    if x==y:
        ans+=1
print(ans)