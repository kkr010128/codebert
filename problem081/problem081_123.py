#!/usr/bin/python3
 
cmdvar_numlist=input()
cmdvar_spritd=cmdvar_numlist.split()
D,T,S=list(map(int,cmdvar_spritd))

if D/S<=T:
    print("Yes")
else:
    print("No")