N=int(input())

ans=[]
while(1):
    if N==0:
        break
    tmp=N%26
    if tmp==0:
        ans.append(26)
        N=N//26-1
    else:
        N//=26
        ans.append(tmp)
        
new_ans = list(reversed(ans))
ANS=""

for i in new_ans:
    ANS+=chr(96+int(i))
print(ANS)