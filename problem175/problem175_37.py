n = int(input())
s = input()

t="RGBRGB"

c=0
cm=0
for i in range(3):
    for j in range(1,n-1):
        if s[j]==t[i] :
            low = s[:j].count(t[i+1])
            high = s[j:].count(t[i+2])
            c += low*high
            low = s[:j].count(t[i+2])
            high = s[j:].count(t[i+1])
            c += low*high
            for k in range(1,j+1):
                if j+k>n-1 :
                    break
                if s[j-k]!=t[i] and s[j+k]!=t[i] and s[j-k]!=s[j+k]:
                    cm+=1


print(c-cm)
