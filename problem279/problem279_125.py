N=int(input())
S=str(input())
flg = True
if len(S)%2 != 0:
    print("No")
else:
    for i in range(len(S)//2):
        if S[i] != S[i+len(S)//2]:
            print("No")
            flg = False
    if flg == True:
        print("Yes")
