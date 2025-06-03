S=input()
T=input()
ls = []
flg = False
for i in range(26):
    #print(S+chr(ord("a")+i))
    #print(type(T),type(S+chr(ord("a")+i)))
    if T == S+chr(ord("a")+i):
        flg = True
        #print("Yes")
        break
    else:
        continue
if flg == True:
    print("Yes")
else:
    print("No")
