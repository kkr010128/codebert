w=raw_input()
ct=0
while 1:
    s=raw_input()
    if s=='END_OF_TEXT':
        break
    s=s.split()
    for i in s:
        if i.lower()==w :
            ct+=1
print(ct)