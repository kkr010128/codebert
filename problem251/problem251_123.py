n,k=map(int,input().split())
R,S,P=map(int,input().split())
T=input()
t=""
count=0
for i in range(n):
    if i>k-1:
        if T[i]=="r":
            if t[i-k]!="p":
                t=t+"p"
                count+=P
            else:
                t=t+" "
        if T[i]=="s":
            if t[i-k]!="r":
                t=t+"r"
                count+=R
            else:
                t=t+" "
        if T[i]=="p":
            if t[i-k]!="s":
                t=t+"s"
                count+=S
            else:
                t=t+" "
    else:
        if T[i]=="r":
            t=t+"p"
            count+=P
        if T[i]=="p":
            t=t+"s"
            count+=S
        if T[i]=="s":
            t=t+"r"
            count+=R
print(count)