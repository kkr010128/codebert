c=[0]*26
while 1:
        try:
                t=list(raw_input().lower())
                for i in range(len(t)):
                        if 0<=ord(t[i])-ord("a")<=25:
                                c[ord(t[i])-ord("a")]+=1
        except EOFError:
                break
for i in range(26):
        print chr(ord("a")+i),":",c[i]