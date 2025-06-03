s=input()
p=input()
b=s
s+=s
ans=0
same_count=0
for i in range(len(b)):
    for j in range(len(p)):
        if s[i+j]==p[j]:
            same_count+=1

    if same_count==len(p):
        ans=1
    same_count=0

if ans==1:
    print("Yes")
else:
    print("No")
