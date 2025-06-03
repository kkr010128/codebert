s=[0]*26
try:
    while True:
        n=str(input())
        n=n.lower()
        #print(n)
        for i in range(len(n)):
            if 97<=ord(n[i])<=122:
                s[ord(n[i])-97]+=1
except EOFError:pass
for j in range(26):
    print(chr(j+97),':',s[j])

