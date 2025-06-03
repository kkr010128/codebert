n = int(input())
full_set=set([1,2,3,4,5,6,7,8,9,10,11,12,13])
S=[]
H=[]
C=[]
D=[]
for i in range(n):
    suit,num = input().split()
    if   suit=="S": S.append(int(num))
    elif suit=="H": H.append(int(num))
    elif suit=="C": C.append(int(num))
    elif suit=="D": D.append(int(num))
S_set=set(S)
H_set=set(H)
C_set=set(C)
D_set=set(D)
for (suit,suit_set) in zip(["S","H","C","D"],[S_set,H_set,C_set,D_set]):
    for num in sorted(list(full_set - suit_set)): print(suit,num)