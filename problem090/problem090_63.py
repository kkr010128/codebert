S=input()
count=[0]
s=0
for i in range(3):
    if S[i]=='R':
        if i==2 or S[i+1]=='S':
            s=s+1
            count.append(s)
            s=0
        else:
            s=s+1
print(max(count))