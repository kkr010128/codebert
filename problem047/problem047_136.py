# coding: utf-8

def toAdd(a, b):
    return int(a) + int(b)
    
def toSubtract(a, b):
    return int(a) - int(b)

def toMultiply(a, b):
    return int(a) * int(b)

def toDivide(a, b):
    return int(int(a) / int(b))
    
operations = {
    "+": toAdd,
    "-": toSubtract,
    "*": toMultiply,
    "/": toDivide
    }

while True:
    valueA, operation, valueB = input().split(" ")
    if operation == "?":
        break
    function = operations[operation]
    print("{0}".format(int(function(valueA, valueB))))