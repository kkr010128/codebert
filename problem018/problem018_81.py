import sys
str = ""
for line in sys.stdin:
	str = line

numbers = str.split()

answer = 0
stackList = []

for number in numbers :

    if number == '+' :
        answer = int(stackList.pop()) + int(stackList.pop())
        stackList.append(answer)
    elif number == '-' :
        x = int(stackList.pop())
        y = int(stackList.pop())
        answer = y - x
        stackList.append(answer)
    elif number == '*' :
        answer = int(stackList.pop()) * int(stackList.pop())
        stackList.append(answer)
    else :
        stackList.append(number)

print(answer)

