while (True):
    code=list(map(int,input().split()))
    if(code[0]==-1 and code[1]==-1 and code[2]==-1):
        break
    sum=code[0]+code[1]    
    if(code[0]==-1 or code[1]==-1):
        print("F")
    elif(sum>=80):
        print("A")
    elif(sum>=65):
        print("B")
    elif(sum>=50):
        print("C")
    elif(sum<30):
        print("F")
    elif(sum>=30 and code[2]>=50):
        print("C")
    else:
        print("D")