import re
S = input()
T = input()
result=0
if(len(S)!=len(T)):
    pass
elif(re.fullmatch(r'[a-z]{1,200000}', S) and re.fullmatch(r'[a-z]{1,200000}', T)):
    for i in range(len(S)):
        if S[i]!=T[i]:
            result+=1
    print(result)