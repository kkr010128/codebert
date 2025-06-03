gusu,kisu=map(int,input().split())
count=0
S=[]
for i in range(gusu):
    S.append(2)
for i in range(kisu):
    S.append(1)

for i in range(len(S)):
    for j in range(len(S)):
        if i!=j and i>j:
            if (S[i]+S[j])%2==0:
                count+=1

print(count)