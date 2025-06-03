alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N=int(input())
S=[0 for i in range(0,N)]
string=''
for i in range(0,N):
    string+='a'
print(string)
digit=N-1
while True:
    if digit!=0:
        if S[digit]==max(S[0:digit])+1:
            digit-=1
        else:
            S[digit]+=1
            for j in range(digit+1,N):
                S[j]=0
            digit=N-1
            if S[0]==1:
                break
            string=[0 for i in range(0,N)]
            for i in range(0,N):
                string[i]=alphabetlist[S[i]]
            print(''.join(string))
    else:
        break