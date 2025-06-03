S = list(map(str, input()))
N = len(S)+1
List = [0]*N
rightcount = 0
leftcount = 0

if S[0] == "<":
    leftcount+=1
else:
    rightcount+=1

for i in range(1, N-1):
    if S[i] == "<":
        leftcount+=1
        if S[i-1] == "<":
            List[i] = List[i-1]+1
        elif S[i-1] == ">":
            for j in range(rightcount):
                List[i-j] = j
            if List[i-rightcount]<=List[i-rightcount+1]:
                List[i-rightcount] = List[i-rightcount+1] + 1
            rightcount = 0


    if S[i] == ">":
        rightcount+=1
        if S[i-1] =="<":
            for j in range(leftcount+1):
                List[i-j] = leftcount - j
            leftcount = 0

if S[N-2] == "<":
    List[N-1] = List[N-2] + 1
else:
    for j in range(rightcount):
        List[N-1-j] = j
    if List[N-1-rightcount]<=List[N-1-rightcount+1]:
        List[N-1-rightcount] = List[N-1-rightcount+1] + 1

print(sum(List))
