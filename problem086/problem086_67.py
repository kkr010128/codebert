#!/usr/bin/python3
 
cmdvar_numlist=input()
cmdvar_numlist_splited=cmdvar_numlist.split()

N,X,T=list(map(int,cmdvar_numlist_splited))

i=0

while N >0:
    N = N - X
    i+=1

ans=T * i
print(ans)