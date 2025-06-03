N = int(input())
s = input()
cnt=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            a=s.find(str(i))
            if a==-1:
                continue
            b=s[a+1:].find(str(j))
            if b==-1:
                continue
            b+=a+1
            c=s[b+1:].find(str(k))
            if c==-1:
                continue
            cnt+=1

print(cnt)
