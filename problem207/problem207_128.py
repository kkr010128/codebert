A=[]
for _ in range(3):
    A.append(list(map(int,input().split())))
n=int(input())
B=[]
for _ in range(n):
    B.append(int(input()))

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

B=get_unique_list(B)
s=0
if A[0][0] in B and A[1][1] in B and A[2][2] in B:
    s+=1
elif A[0][2] in B and A[1][1] in B and A[2][0] in B:
    s+=1
else:    
    for i in range(3):
        if A[0][i] in B and A[1][i] in B and A[2][i] in B:
            s+=1
        elif A[i][0] in B and A[i][1] in B and A[i][2] in B:
            s+=1

if s>=1:
    print("Yes")
else:
    print("No")
