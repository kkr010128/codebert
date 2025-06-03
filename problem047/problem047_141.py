# coding: utf-8

while True:
    valueA, operation, valueB = input().split(" ")
    if operation == "?":
        break
    elif operation == "+":
        result = int(valueA) + int(valueB)
    elif operation == "-":
        result = int(valueA) - int(valueB)
    elif operation == "*":
        result = int(valueA) * int(valueB)
    elif operation == "/":
        result = int(valueA) / int(valueB)
    print("{0}".format(int(result)))