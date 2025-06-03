N = int(input())
S = input()
if N%2 == 1:
    print("No")
else:
    a = 0
    for i in range(N//2):
        if S[i] != S[N//2+i]:
            a += 1
    if  a == 0:
        print("Yes")
    else:
        print("No")