s=input()
for i in range(int(input())):
    sou_com=input().split()
    if sou_com[0]=='print':
        print(s[int(sou_com[1]):int(sou_com[2])+1])
    elif sou_com[0]=='reverse':
        s=s[:int(sou_com[1])]\
        +s[int(sou_com[1]):int(sou_com[2])+1][::-1]\
        +s[int(sou_com[2])+1:]
    elif sou_com[0]=='replace':
        s=s[:int(sou_com[1])]\
        +sou_com[3]\
        +s[int(sou_com[2])+1:]