n=int(input())
s=input()
ans=0
for i in range(10):
    if str(i) in s[:-2]:
        s1=s.index(str(i))

        for j in range(10):
            if str(j) in s[s1+1:-1]:
                s2=s[s1+1:].index(str(j))+s1+1

                for k in range(10):
                    if str(k) in s[s2+1:]:
                        ans+=1

print(ans)
