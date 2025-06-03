s=input()
t=input()
i=len(s)-1
counter=0
while i>=0:
    if s[i]!=t[i]:
        counter+=1
    i=i-1
print(counter)