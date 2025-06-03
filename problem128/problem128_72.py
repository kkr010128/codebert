X,N =  map(int,input().split())
N_List = list(map(int,input().split()))
ct = 0
pos = 0
while True:
    if pos == 0:
        if X not in N_List:
            ans = X
            break
        else:
            pos += 1
    elif pos > 0:
        if X-pos not in N_List:
            ans = X - pos
            break
        elif X + pos not in N_List:
            ans = X + pos
            break
        else:
            pos += 1
print(ans)