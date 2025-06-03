#B
S=input()

N=len(S)
con_2=S[:(N-1)//2]
con_3=S[((N+3)//2-1):]

if S==S[::-1] and con_2==con_2[::-1] and con_3==con_3[::-1]:
            print('Yes')
else:
    print('No')