H,W,K = map(int,input().split(sep=" "))
S = [list(map(int,list(input()))) for i in range(0,H,1)]
minimum = H+W
for sepH in range(0,2**(H-1),1):
    bitcounter = 0
    tmp_sepH = sepH
    while tmp_sepH > 0:
        if tmp_sepH & 1 == 1:
            bitcounter+=1
        tmp_sepH = tmp_sepH//2
    A = [[0 for i in range(0,W,1)] for j in range(0,bitcounter+1,1)]
    index=[[]for i in range(0,bitcounter+1,1)]
    countInd = 0
    for i in range(0,H,1):
        index[countInd].append(i)
        if (sepH >> i) & 1:
            countInd +=1
   
    for j in range(0,bitcounter+1,1):
        for i in range(0,W,1):
            for k in range(0,len(index[j]),1):
                if S[index[j][k]][i] == 1:
                    A[j][i]+=1
    countA=[0 for i in range(0,bitcounter+1,1)]
    sepCounter = 0
    dame = False
    for i in range(0,W,1):
        for j in range(0,bitcounter+1,1):
            if A[j][i] > K:
                dame = True
        for j in range(0,bitcounter+1,1):
            countA[j]+=A[j][i]
            if countA[j] > K:
                sepCounter+=1
                for j in range(0,bitcounter+1,1):
                    countA[j] = A[j][i]
                break

    if bitcounter+sepCounter < minimum and (not dame):
        minimum = bitcounter +sepCounter

print(minimum)