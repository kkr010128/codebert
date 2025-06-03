S=input()
l=len(S)
a=0
for i in range(int(l/2)):
    if S[i]!=S[-(i+1)]:
        a+=1
print(a)