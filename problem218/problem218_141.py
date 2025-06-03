N=int(input())

ls={}
max_ch=0
for i in range(N):
    ch=input()
    if not ch in ls:
        ls[ch]=1
    else:
        ls[ch]+=1
    if max_ch<ls[ch]:
        max_ch=ls[ch]

S=[]
for j in ls:
    if max_ch==ls[j]:
        S.append(j)

S=sorted(S)

for i in S:
    print(i)