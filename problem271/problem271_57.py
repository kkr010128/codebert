N=int(input())
S=input()
l=len(S)
a=''
for i in range(l):
    if ord(S[i])+N>90:
        a+=chr(ord(S[i])+N-26)
    else:
        a+=chr(ord(S[i])+N)
print(a)