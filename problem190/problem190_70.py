S = input()
flag = 0
for i in range(0,len(S)//2):
    if S[i] == S[-1-i]:
        continue
    else:
        flag = 1
        print("No")
        break
if flag == 0:
    S = S[:((len(S)-1)//2)]
    for i in range(0,len(S)//2):
        if S[i] == S[-1-i]:
            continue
        else:
            flag = 1
            print("No")
            break
if flag == 0:
    print("Yes")