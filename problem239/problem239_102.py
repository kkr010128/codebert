S=input()
I="abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    if S==I[i]:
        print(I[i+1])
        exit()

