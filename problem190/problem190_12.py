S=input()
N=len(S)
A=S[:(N-1)//2]
B=S[(N+3)//2-1:]
if S!=S[::-1] or A!=A[::-1] or B!=B[::-1]:
    print("No")
else:
    print("Yes")