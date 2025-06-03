n = input()
Max = -4300000000
Min = input()
for i in range(n - 1):
    IN_NOW = input()

    Max = max(Max, (IN_NOW - Min))    
    Min = min(Min, IN_NOW)
    
print Max