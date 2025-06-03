M=[]
F=[]
R=[]
while True:
    m,f,r=map(int,raw_input().split())
    if (m,f,r)==(-1,-1,-1):
        break
    else:
        M.append(m)
        F.append(f)
        R.append(r)
for i in range(len(M)):
    sum=M[i]+F[i]
    if M[i]==-1 or F[i]==-1:
        print('F')
    elif sum>=80:
        print('A')
    elif sum>=65:
        print('B')
    elif sum>=50:
        print('C')
    elif sum>=30:
        if R[i]>=50:
            print('C')
        else:
            print('D')
    else:
        print('F')