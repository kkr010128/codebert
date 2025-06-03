S=input()
N=int(input())
for i in range(N):
    command=input().split()
    if command[0]=="replace":
        a=int(command[1])
        b=int(command[2])
        x=command[3]
        A=S[:a]
        B=S[b+1:]
        S=A+x+B
    elif command[0]=="reverse":
        a=int(command[1])
        b=int(command[2])
        A=S[:a]
        B=S[a:b+1]
        C=S[b+1:]
        T=""
        for p in range(len(B)):
            T+=B[len(B)-1-p]
        S=A+T+C
    else:
        #command[0]=="print"
        a=int(command[1])
        b=int(command[2])
        print(S[a:b+1])

