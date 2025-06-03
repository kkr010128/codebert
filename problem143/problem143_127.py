n=int(input())
w=input()
alen=len(w)
blen=len(w)

if blen > n:
    
    print(w[:n]+"..." )
else:
    print(w)