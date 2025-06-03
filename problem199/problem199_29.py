S=input()
flg = True
for i in range(len(S)):
    if len(S)%2 == 1:
        flg = False
        break
    if i%2==0:
        if S[i]+S[i+1] != "hi":
            flg = False

if flg == True:
    print("Yes")
else:
    print("No")