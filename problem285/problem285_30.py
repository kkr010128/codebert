import sys
S = list(input())
lis = [0] * (len(S)+1)
 
if len(S) == 1:
    print(1)
    sys.exit()
 
 
#最初は < を処理する
for i in range(len(S)):
    if S[i] == "<":
        lis[i+1] = lis[i] + 1
 
 
 
 
for j in range(len(S)-1,-1,-1):
    if S[j] == ">":
        lis[j] = max(lis[j],lis[j+1] + 1)
 
 
 
print(sum(lis))