S = list(input())
front_S = S[:(len(S)//2)]
S.reverse()
back_S=S[:(len(S)//2)]
count = 0
for i,j in zip(front_S,back_S):
    if(i!=j):
        count+=1
print(count)