w=raw_input().lower()
c=0
while 1:
        t=map(str,raw_input().split())
        if t[0]=="END_OF_TEXT":
                break
        for i in range(len(t)):
                if t[i].lower()==w:
                        c+=1
print c