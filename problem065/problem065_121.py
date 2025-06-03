# coding: utf-8
# Here your code !

def func():
    try:
        word=input().rstrip().lower()
        words=[]
        while(True):
            line=input().rstrip()
            if(line == "END_OF_TEXT"):
                break
            else:
                words.extend(line.lower().split(" "))
    except:
        return inputError()

    print(words.count(word))
    

def inputError():
    print("input Error")
    return -1
 
func()