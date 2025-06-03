N=int(input())
S=input()
s=[]
for i in S:
    T=ord(i) - ord('A') + 1+N+64
    if T<=90:
        t=T
    else:
        t=T-26
    s.append(chr(t))
print(*s,sep='')