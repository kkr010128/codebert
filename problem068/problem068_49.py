def run():
    s=input()
    command_num=int(input())
    
    for i in range(command_num):
        command = input().split()
        command = list(map(lambda x: int(x) if x.isdigit() else x,command))
        
        # print(s)
        if command[0] == "print":
            a=command[1]
            b=command[2]
            print(s[a:b+1])
            
        elif command[0] == "reverse":
            a=command[1]
            b=command[2]
            
            rev=s[a:b+1]
            rev=rev[::-1]
            #境界処理がめんどくさい
            pre= "" if a==0 else s[0:a]
            post="" if b==len(s)-1 else s[b+1:]
            
            s=pre+rev+post
            
            
        elif command[0] == "replace":
            a=command[1]
            b=command[2]
            p=command[3]
            #境界処理がめんどくさい
            pre= "" if a==0 else s[0:a]
            post="" if b==len(s)-1 else s[b+1:]
            
            s=pre+p+post
            
        else:
            assert False

run()
