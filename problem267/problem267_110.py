N=int(input())
S=input()
kouho=[]
for n in range(1000):
    st=str(n)
    if len(st)<=2:
        st='0'*(3-len(st))+st
    kouho.append(st)
ans=0
for k in kouho:
    number=0
    for s in S:
        if k[number]==s:
            number+=1
        if number==3:
            break
    if number == 3:
        ans += 1
print(ans)
