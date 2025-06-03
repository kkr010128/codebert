num = 100000

n = int(input())
for i in range(n):
    num*=1.05
    
    if num % 1000 >= 1 :
        a = num % 1000
        num = int(num+1000-a)
    else:
        num = int(num)
        
        
print(num)

