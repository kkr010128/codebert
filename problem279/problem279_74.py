N = int(input())
S = input()

if len(S) % 2 == 0 :
    for i in range(len(S)//2) :
        if S[i] != S[i+len(S)//2] :
            print("No")
            exit()
    print("Yes")
    exit()
print("No")