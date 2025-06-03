s=input()
s+='?'
x=[]
ch=1
if s[0]=='>':
    x.append(0)
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        ch+=1
    else:
        x.append(ch)
        ch=1
x.append(0)
a=0
for i in range(len(x)-1):
    if i%2==0 and x[i]<=x[i+1]:
        a+=x[i+1]
        for j in range(x[i]):
            a+=j
        for j in range(x[i+1]):
            a+=j
    elif i%2==0 and x[i]>x[i+1]:
        a+=x[i]
        for j in range(x[i]):
            a+=j
        for j in range(x[i+1]):
            a+=j
if (len(x)-1)%2==1:
    for j in range(x[len(x)-1]):
        a+=j
print(a)
