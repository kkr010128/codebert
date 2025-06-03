s=[]
for i in raw_input().split():
    if i<"0":
        t=s.pop()
        s.append(str(eval(s.pop()+i+t)))
    else:
        s.append(i)
print s[0]