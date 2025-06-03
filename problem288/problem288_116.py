n = int(input())

m = 0
for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            m = i
            
x = m
y = n/m
print(int(x-1 + y-1))