
t=input()
s1=[]
s2=[]
pond=[]
totalsum=0

for i in range(len(t)):
    if t[i]=="\\" :
        s1.append(i)
    elif t[i]=="/" and len(s1)!=0:
        p1=s1.pop()
        sum=i-p1
        totalsum+=sum
        while len(s2)>0:
            if s2[-1]>p1:
                s2.pop()
                sum+=pond.pop()
            else:
                break
        pond.append(sum)
        s2.append(i)


print(totalsum)
print(len(pond),*pond)


