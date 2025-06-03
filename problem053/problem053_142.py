# coding: utf-8
# Here your code !

def func():
    try:
        line = input()
        line = input().rstrip()
        numbers = line.split(" ")
    except:
        print("input error")
        return -1
        
    numbers.reverse()
    result=""
    for item in numbers:
        result += item+" "
    
    print(result.rstrip(" "))

func()