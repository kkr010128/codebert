k=0
n=input()
n=n.lower()
s=input()
while s!='END_OF_TEXT':
    s=s.lower()
    S=s.split()
    #print(S)
    for i in range(len(S)):
        if n==S[i]:
            k+=1
    s=input()
print(k)
