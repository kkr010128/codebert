S = input()
N = len(S)
flag = [0,0,0]


if S=="".join(reversed(list(S))):
    flag[0]=1
if S[:int((N-1)/2)]=="".join(reversed(list(S[:int((N-1)/2)]))):
    flag[1]=1
if S[int((N+3)/2)-1:]=="".join(reversed(list(S[int((N+3)/2)-1:]))):
    flag[2]=1
print("Yes" if flag==[1,1,1] else "No")
