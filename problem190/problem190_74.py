S = input()
N = len(S)
flag = True

if S!="".join(reversed(list(S))):
    flag=False
if S[:int((N-1)/2)]!="".join(reversed(list(S[:int((N-1)/2)]))):
    flag=False
print("Yes" if flag else "No")
