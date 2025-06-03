s=[i for i in input().split()]
k=[]

for i in range(len(s)):
    if s[i]=="+":
        b=k.pop()
        a=k.pop()
        k.append(int(a)+int(b))
    elif s[i]=="-":
        b=k.pop()
        a=k.pop()
        k.append(int(a)-int(b))
    elif s[i]=="*":
        b=k.pop()
        a=k.pop()
        k.append(int(a)*int(b))

    else:
        k.append(s[i])

print(k[0])
