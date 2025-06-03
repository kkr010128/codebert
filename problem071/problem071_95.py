import os,sys

s=input()
n=len(s)
if s[n-1]=='s':
    s=s+'es'
else:
    s=s+'s'

print(s)