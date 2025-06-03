K = input()
S = input()
LS = len(S)
IK = int(K)

if LS <= IK:
    print(S)

elif LS > IK:
    print(S[0:IK] + '...')
