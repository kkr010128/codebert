N,M = map(int,input().split())
L = [list(map(int,input().split())) for i in range(M)]
dict = {}
 
if M == 0 :
    if N == 1 :
        print(0)
    else :
        print(10**(N-1))
    exit()
 
for x in L :
    dict.setdefault(x[0],[])
    dict[x[0]].append(x[1])
dict.setdefault(1,[1])
 
for k,v in dict.items():
    dict[k] = set(v)
 
ansList = ["0"]*N
for i in range(N) :
    if i+1 in dict :
        ansList[i] = str(list(dict[i+1])[0])
 
isZeroHead = 2 <= N and ansList[0] == "0"
isOverlapping = any([ 2 <= len(v) for v in dict.values()])  
ans = -1 if isZeroHead or isOverlapping else int("".join(ansList))
 
# print(dict)
# print("isZeroHead :",isZeroHead)
# print("isOverlapping :",isOverlapping)
print(ans)