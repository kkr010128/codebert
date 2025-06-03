exp  = input().split()
stk = []

for i in exp :
    if i in ('+', '-', '*') :
        num1 = stk.pop()
        num2 = stk.pop()
        
        if i == '+' :
            stk.append(str(int(num1) + int(num2)))
        elif i == '-' :
            stk.append(str(int(num2) - int(num1)))
        else :
            stk.append(str(int(num2) * int(num1)))            
    else :
        stk.append(i)
        
print(stk.pop())
