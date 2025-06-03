S = input()
q = int(input())
for i in range(q):
    cmd = input().split()
    a = int(cmd[1])
    b = int(cmd[2])
    
    if cmd[0] == "print":
        print(S[a:b+1])
        
    elif cmd[0] == "replace":
        S = S[0:a] + cmd[3] + S[b+1:len(S)]
    
    elif cmd[0] == "reverse":
        r = S[a:b+1]
        S = S[0:a] + r[::-1] + S[b+1:len(S)]
        
        
