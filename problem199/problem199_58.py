S = input()


flg = True

for i in range(len(S)):
    if flg == True and S[i] == "h":
        flg = False
        continue
    elif flg == False and S[i] == "i":
        flg = True
        continue
    else:
        print("No")
        break
else:
    if flg == False:
        print("No")
    else:
        print("Yes")