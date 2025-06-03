T=int(input())
S=str(input())
s=len(S)
if s<=T:
    print(S)
else:
    print(S[:T]+'...')