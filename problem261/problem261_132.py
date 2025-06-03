s=input()
n=len(s)//2

s1=s[:n]
s2=s[-n:]
s2=s2[::-1]

cnt=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        cnt+=1

print(cnt)
