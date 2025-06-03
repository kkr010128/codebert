N=int(input())
S=str(input())
ls = []
for i in range(len(S)):
    ls.append(S[i])
for i in range(len(S)):
    x = S[i]
    #print(ord(x)+N,ord("Z"))
    if ord(x)+N > ord("Z"):
        #print("if")
        #print(ord("A")-ord("Z")+(ord(x)+N))
        ls[i]=chr(ord("A")-ord("Z")+(ord(x)+N)-1)
    else:
        #print("else")
        ls[i]=chr((ord(x)+N))
print("".join(ls))
