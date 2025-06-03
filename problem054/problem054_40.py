# coding: utf-8
# Here your code !

def func():
    try:
        line = input()
    except:
        print("input error")
        return -1
        
    marks = ("S","H","C","D")
    cards = []
    while(True):
        try:
            line = input().rstrip()
            elements = line.split(" ")
            if(elements[0] in marks):
                elements[1]=int(elements[1])
                cards.append(elements)
            else:
                print("1input error")
                return -1
        except EOFError:
            break
        except :
            print("input error")
            return -1
    
    result=""
    for mark in marks:
        for i in range(1,14):
            if([mark,i] not in cards):
                result += mark+" "+str(i)+"\n"
    if(len(result)>0):
        print(result.rstrip())
func()