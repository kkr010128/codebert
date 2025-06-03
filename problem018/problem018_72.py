#coding:utf-8
#1_3_A
formula = input().split()
stack = []
for char in formula:
    if char.isdigit():
        stack.append(char)
    else:
        ans = str(eval(stack.pop(len(stack)-2) + char + stack.pop()))
        stack.append(ans)
print(stack.pop())