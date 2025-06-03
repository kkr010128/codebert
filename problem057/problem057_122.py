# coding: utf-8
# Here your code !

def func():
    data=[]
    while(True):
        try:
            line=[ int(item) for item in input().rstrip().split(" ") ]
            if(line == [-1, -1, -1]):
                break
            data.append(line)
        except EOFError:
            break
        except:
            return inputError()

    result=""
    for score in data:
        if( (score[0]<0) or (score[1]<0)):
            result+="F\n"
        elif(score[0]+score[1] >= 80):
            result+="A\n"
        elif(score[0]+score[1] >= 65):
            result+="B\n"
        elif(score[0]+score[1] >= 50):
            result+="C\n"
        elif(score[0]+score[1] >= 30):
            if(score[2] >= 50):
                result+="C\n"
            else:
                result+="D\n"
        else:
            result+="F\n"
    
    print(result.rstrip())

def inputError():
    print("input error")
    return -1

func()