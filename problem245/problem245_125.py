N = int(input())
S = str(input())

s=list(S)  
num=0
for i in range(N-2):
    if s[i]=='A' and s[i+1]=='B' and s[i+2]=='C':
        num+=1
print(num)