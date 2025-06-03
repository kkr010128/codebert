n = int(input())
result = 100000
for i in range(0,n):
    result = result * 1.05
    if result % 1000 == 0:
        pass
    else:
        result = result-(result % 1000)+ 1000
        result = int(result)
print(result)