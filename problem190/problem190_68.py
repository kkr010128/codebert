S = input()
N = len(S)
flag = True

if S!=S[::-1]:
    flag=False
if S[:int((N-1)/2)]!=S[:int((N-1)/2)][::-1]:
    flag=False
print("Yes" if flag else "No")
